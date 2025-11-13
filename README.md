# Replication Package for "From Constraints to Construction: A Modelling Procedure for Generating Coherent Business Architecture Models"

This repository contains the full set of artefacts for the research paper submitted to the Thirty-Fourth European Conference on Information Systems (ECIS 2026). It provides all prompts, execution scripts, analysis scripts, and raw data necessary to fully replicate the experiments described in the paper.

## Repository Structure

The repository is organized into three main directories:

- **/prompts**: Contains the modular Markdown files that constitute the prompts for all experimental conditions.
- **/scripts**: Contains the Python scripts used to execute the experiments and the JavaScript files used for model validation and visualization.
- **/runs**: Contains the complete, raw output of all 12 experimental runs discussed in the paper, organized by LLM platform and sector case.

---

## Methodology Overview

### 1. Prompts

The prompts are constructed in a modular fashion to ensure consistency.

- `prompts/C.md` is the single-turn, algorithmic prompt for **Condition C (Constructive Procedure)**.
- `prompts/AB.md` is the base file for **Condition A (Naive Generation)** and **Condition B (Declarative Validation & Repair)**. To create the final, executable prompt for these conditions, this base file must be manually assembled with other modules (e.g., `constraints.md`, `repair.md`). Instructions for assembly are provided as comments within the files (e.g., `<!-- CONDITION B: INSERT CONSTRAINTS.MD -->`).

### 2. Scripts

- `scripts/open-ai.py` & `scripts/gen-ai.py`: Python scripts to execute the experiments against the OpenAI and Google Generative AI APIs, respectively. **They expect a single, fully assembled prompt file as input.** They then call the API and save all relevant output files to a new directory under `/runs`.
- `scripts/jArchi-validator.js`: A script for the [jArchi plugin](https://www.archimatetool.com/plugins/) in the Archi modelling tool. After manually importing a model from the generated CSV files into Archi, this script runs the validation logic to calculate the **Formal Correctness** and **Cross-stream Utilization Index (CUI)** metrics.
- `scripts/jArchi-draw.js`: A jArchi utility script to automatically render a manually imported model on an Archi diagram, providing a quick visual impression of its structure.

### 3. Runs

Each experimental run is stored in a dedicated folder following the structure: `/runs/[LLM_Platform]/[Sector_Case]/`. Each individual run folder contains the following files, timestamped for uniqueness:

- `..._prompt.md`: The exact, fully assembled prompt sent to the API.
- `..._response.md`: The raw response received from the LLM.
- `..._metadata.json`: Metadata about the run, including model parameters and execution time.
- `..._elements.csv`, `..._relations.csv`, `..._properties.csv`: The structured model data, parsed from the LLM's response, ready for validation.

---

## How to Replicate the Experiment

### Prerequisites

1. **Python 3.9+** with required libraries (e.g., `openai`, `google-generativeai`, `python-dotenv`).
2. **API Keys** for OpenAI and/or Google AI Studio.
3. **Archi**: The open-source modelling tool (version 5.x).
4. **jArchi**: The scripting plugin for Archi.

### Step 1: Configuration

1. Clone this repository.
2. Add your API keys as environment variables:
   ```
   OPENAI_API_KEY=...
   GEMINI_API_KEY=...
   ```

### Step 2: Running the Generation Scripts

1. **Assemble the prompt:** Manually create a final prompt file by combining the modules in the `/prompts` directory as instructed by the comments.
2. **Execute the experiment:** Edit the Python script to point to the assembled prompt file and run it from your terminal.

**Example for Condition C (OpenAI):**

```bash
python scripts/open-ai.py
```

A new folder containing all output files will be created in the `/llm_runs_openai` directory.

### Step 3: Validating and Visualizing the Results

1. Open the Archi application.
2. Import the generated CSV files.
3. Open the jArchi scripting console.
4. Load and run the `scripts/jArchi-validator.js` script.
5. The script will output the validation report, including the final metrics, in the console.
6. Similarly, run `scripts/jArchi-draw.js` to visualize the model on the `Default View` diagram.

---

## Citation

If you use these artefacts or build upon our research, please cite our paper:

```bibtex
@inproceedings{
  TODO
}
```

## License

The content of this repository is licensed under the MIT License. See the `LICENSE` file for details.
