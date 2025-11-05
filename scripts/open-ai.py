import os
from openai import OpenAI
import json
import time
import re

# --- Setup and Client Init ---
try:
    API_KEY = os.environ.get("OPENAI_API_KEY") # <-- GEWIJZIGD: Variabele naam
    if not API_KEY:
        # Dit is de aanbevolen manier om de API Key te hanteren in de OpenAI SDK
        raise ValueError("OPENAI_API_KEY environment variable not set.")
    
    # NIEUW: Initialisatie van de OpenAI Client
    client = OpenAI(api_key=API_KEY) 
except Exception as e:
    print(f"Setup Fout: {e}")
    exit()
# -----------------------------


# --- Parameters  ---
MODEL_NAME = "gpt-5"
SYSTEM_INSTRUCTION = "You are an experienced business architect. Adhere strictly to all instructions and provide output in the exact requested format."
REASONING = "medium"
VERBOSITY = "low"
# ---------------------------------------------


def run_llm_experiment_openai(prompt_name: str, prompt_text: str):
    """Voert de LLM-call uit met de OpenAI API."""
    
    print(f"\n--- Running Experiment: {prompt_name} (OpenAI) ---")
    
    output_dir = "llm_runs_openai"
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # 2. API Call (GEWIJZIGD)
        response = client.responses.create(
            model=MODEL_NAME,
            reasoning={"effort": REASONING},
            text={"verbosity": VERBOSITY},
            input=[
                {"role": "developer", "content": SYSTEM_INSTRUCTION},
                {"role": "user", "content": prompt_text},
            ]
        )
        
        # 3. Extraheer de Output Tekst (GEWIJZIGD)
        llm_response_text = response.output_text

        # 4. Verzamel Alle Data (Metadata aanpassing)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        base_filename = os.path.join(output_dir, f"{prompt_name}_{timestamp}")
        
        # --- Metadata en Usage (GEWIJZIGD om OpenAI structuur te reflecteren) ---
        metadata_content = {
            "prompt_name": prompt_name,
            "timestamp": timestamp,
            "model": response.model,
            "reasoning": response.reasoning.effort,
            "verbosity": response.text.verbosity,
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens, 
            "total_tokens": response.usage.total_tokens,
            "system_instruction": SYSTEM_INSTRUCTION
        }
        
        # Schrijf Metadata als JSON
        with open(f"{base_filename}_metadata.json", "w") as f:
            json.dump(metadata_content, f, indent=4)


        # --- Full Prompt Archief (Blijft hetzelfde) ---
        with open(f"{base_filename}_prompt.md", "w", encoding="utf-8") as f:
            f.write(f"# Prompt for {prompt_name}\n\n```markdown\n{prompt_text}\n```\n")


        # --- CSV Extractie en Opslag (Gebruikt de nieuwe tekst variabele) ---
        csv_contents = re.findall(
            r'^```csv\n(.*?)\n```$', 
            llm_response_text,
            re.DOTALL | re.MULTILINE
        )
        
        csv_suffixes = ["_elements", "_relations", "_properties"]

        if len(csv_contents) == 3:
            for i, content in enumerate(csv_contents):
                csv_filename = f"{base_filename}{csv_suffixes[i]}.csv"
                with open(csv_filename, "w", encoding="utf-8") as f:
                    f.write(content.strip() + "\n") 
                print(f"  Extracted CSV saved: {os.path.basename(csv_filename)}")
        else:
            print(f"WAARSCHUWING: Verwacht 3 CSV blokken, maar vond er {len(csv_contents)}. Geen afzonderlijke CSV's opgeslagen.")
        
        
        # --- Raw Response Archief ---
        with open(f"{base_filename}_response.md", "w", encoding="utf-8") as f:
            f.write(f"# Raw LLM Response for {prompt_name}\n\n")
            f.write(llm_response_text)
            
        print(f"Succesvol opgeslagen: {base_filename}_response.md en metadata.")

    except Exception as e:
        print(f"Fout tijdens API-call voor {prompt_name}: {e}")


if __name__ == "__main__":
    def load_prompt(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Fout: {filename} niet gevonden. Zorg dat uw prompt bestanden klaarliggen.")
            return None

    prompt = load_prompt("Prompt.txt") 
    
    if prompt:
        run_llm_experiment_openai("Condition_C", prompt)