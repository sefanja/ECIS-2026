# Prompt for Condition_C

```markdown
# Reference Architecture Design Brief

## Part 1: Context & Scope

You are an experienced business architect tasked with creating a business architecture reference model for a particular sector. To ground the model in strategic purpose, your first task is to create a concise yet complete Sector Context Profile.

### Sector Context Profile

**Sector to be Analyzed:** Energy Grid Operators

* **Core Purpose & Societal Role:** Describe the sector's fundamental purpose. Why does it exist? What societal need does it fulfill?
* **Primary Business Model Archetype(s):** Identify the dominant business model. Think in terms of B2C (to consumers), B2B (to businesses), B2G (to government), or non-profit/public funding. A hybrid model is possible.
* **Key Strategic Drivers & Basis of Competition:** On what basis do organizations in this sector compete? Consider factors like reputation, innovation, efficiency, customer satisfaction, or societal impact. Name the 2-3 most important ones.
* **Dominant Environmental Factors:** Describe the context in which the sector operates. Consider laws and regulations, public accountability, technological trends, or funding models (e.g., public funds).

## Part 2: Modeling Procedure

**Core Principle: Consistency by Construction**
This procedure is designed to construct a model that is coherent by design. Follow the steps precisely to build the different architectural views from a single, canonical capability model that serves as the "anchor".

**General Instruction on Brevity**
Throughout this entire procedure, do not add any conversational text, summaries, or explanations. Your response must consist only of the specific data deliverables requested in each step.

You will now apply this procedure to create the detailed architectural model for the sector defined in Part 1.

### Step 1: Define the Strategic L0 and L1 Capability Hierarchy (The ANCHOR)

1. **Define L0 Capability:** Generate a single L0 `Capability` for the entire organization, describing its overall value-creating activity using a **Verb-Plural Noun** format (e.g., `Deliver Products and Services`).
2. **Define L1 Capabilities:** Identify 3-7 core, sector-specific L1 `Capabilities`. These management domains must collectively span the entire organization, explicitly excluding generic enabling functions such as Human Resources, Finance, and IT. Use the **Verb-Plural Noun** format to describe the value-creating activity.
   * **Quality Criteria:**
     * Determine a number of L1 `Capabilities` (between 3 and 7) that accurately reflects the complexity of the sector described in Part 1.
     * The L1 Capabilities must be **MECE** (Mutually Exclusive and Collectively Exhaustive): they should minimize overlap in scope while collectively covering the organization's entire value chain.
     * **Mandatory Classification:** Each defined L1 `Capability` must be explicitly assigned to one, and only one, of the following three mutually exclusive categories, thereby ensuring the clear separation of external exchange from internal core activities:
       1. **Value Exchange with Value Suppliers** (Supply Chain activities)
       2. **Core Value Transformation** (The company's unique value-add activities)
       3. **Value Exchange with Value Receivers** (Customer interaction, billing, contracting, etc.)
3. **Present L1 Capabilities:** Explicitly list all L1 `Capabilities` with their classification.

### Step 2: Define the L0 Value Streams

1. Identify **2-3 primary, external `Customer Segments`** for the defined sector.
2. For **each** `Customer Segment`, describe the core `Value Proposition` it receives from the organization. Focus on the ultimate value for the customer.
3. **Define L0 Value Streams using CODP:** Based on the customer segments and their value propositions, define the complete set of L0 `ValueStreams`.
   * **Principle:** If the organization creates a standardized, reusable business asset 'to stock' (**Make-to-Stock, MTS**), this is a separate L0 `ValueStream`. The flow triggered by a customer order (**Assemble-to-Order, ATO**) is another.
   * **Litmus Test:** Ask "Does the organization build a core asset *before* any specific customer is known?"
     * **Example:** A software company develops a standard `Platform` (MTS) before a client signs up. Configuring that platform for a new client (ATO) is a separate L0 Value Stream.
   * **Action:** Use this logic to define all internal asset-creation streams (MTS) and all customer-facing delivery streams (ATO/ETO).
4. **Characterize All Value Streams:** For every L0 `ValueStream` defined above:
    * Assign a `Value Stream Pattern (CODP)`: Choose one of `ETO`, `ATO`, or `MTS`.
    * Use the 'deepest' pattern (`ETO` > `ATO` > `MTS`) that represents a typical case for the sector.
5. Present the result as a list: `[L0 Value Stream Name, Description, Originating VP, Value Stream Pattern]`.

### Step 3: Discover L2 Capabilities and Value Stream Stages Iteratively

You will now analyze each L0 `ValueStream` one by one to discover the complete set of capabilities.

**Procedure:**
Execute the following process for each L0 `ValueStream`. You **must** process the `MTS` (Make-to-Stock) streams first before processing any `ATO` (Assemble-to-Order) or `ETO` (Engineer-to-Order) streams. This ensures that foundational, reusable capabilities are discovered first.

For each L0 `ValueStream`:

1. **Deconstruct into Stages:** Deconstruct the L0 `ValueStream` into a logical sequence of stages. Determine the number of stages required to narrate the complete and highly granular value creation process. Asign a `Sequence` number to each L2 stage (starting from "1" for each L0 stream).
2. **Ensure Lifecycle Completeness:** For an `ATO` or `ETO` stream, verify that the sequence of stages covers the following logical phases. If not, add the necessary stages:
   * **Engagement & Acquisition:** Initial contact, qualification, and agreement.
     * **Core Value Delivery:** The central activities the customer is paying for.
     * **Counter-Performance:** Securing the reciprocal value (e.g., `Process Payment`, `Collect Fee`).
     * **After-Care & Support:** Post-delivery support and issue resolution.
3. **Identify Primary Capabilities:** For each L2 `ValueStream` stage, identify the primary L2 `Capability` it manifests. Adhere to the following rules:
   * **Naming Convention:** Adhere to the **Verb-Plural Noun** format (e.g., `Assess Customer Needs`, `Develop New Products`).
   * **Granularity Rule:** The capability must be defined as a context-free core competency of the organization, such that it can potentially be reused in other value streams, but specific enough that it manifests as only **one** L2 stage within the same L0 value stream.
     * **Litmus Test:** If you are tempted to assign the same capability to multiple stages of the same L0 value stream (e.g., assigning `Manage Service Requests` to both "Receive Request" and "Fulfill Request"), your capability is too broad. You must define more granular capabilities instead (e.g., `Process Intake Requests` and `Deliver Services`).
   * **Assign one Parent:** Assign the newly created L2 `Capabilities` to **exactly one** L1 `Capability` parent.
4. **Discover Supporting Capabilities (First Level):** For each primary L2 `Capability` you just identified, list its 1-3 most critical, direct supporting L2 `Capabilities` (or a justified 0). Adhere to the **naming convention** and the following rules:
   * **Reuse First:** Before defining a new capability, **always check if a suitable one has already been discovered** in a previous step or value stream. A primary capability in one value stream can be reused as supporting in another.
   * **The Value-Flow Direction Rule (Refined):** Support must flow strictly from foundational/stable (Provider) capabilities to operational/dynamic (Consumer) capabilities. The relationship is Provider -> Consumer (Serves). Check: Is the Provider a more generic, infrastructure-like, or policy-setting capability that the Consumer depends on?
     * **Example:** `Define Pricing Strategies` (Provider) -> `Create Customer Quotes` (Consumer).
   Strictly avoid having an operational capability serve a foundational one.
   * **Core Domain Mandate:** You **must** focus exclusively on core capabilities. Strictly avoid generic administrative capabilities (IT, HR, Legal, Finance).
   * **Assign one Parent:** Assign any newly created L2 `Capabilities` to **exactly one** L1 `Capability` parent.
5. **Discover Deeper Supporting Capabilities (Second Level):** Now, for each **newly discovered supporting capability** from the previous step, repeat the process: identify its 1-2 most critical supporting L2 `Capabilities` (or a justified 0), adhering to the **naming convention**, **reuse first**, **value-flow direction**, and **core domain mandate** mentioned above.
   * **Assign one Parent:** Assign any newly created L2 `Capabilities` to **exactly one** L1 `Capability` parent.
6. **Mandatory Output Consolidation Checkpoint:** Before proceeding to Step 4, all discovered elements must be consolidated. This checkpoint does *not* generate a CSV code block. It is a mandatory internal step to ensure completeness before final output generation.
   1. **Consolidate All Capabilities:** Generate a complete list of all Capabilities (L0, L1, and L2) created in Step 1 and Step 3, including their Parent ID. This canonical list is the definitive source for all `Capability` records in the final `elements.csv`.
   2. **Consolidate All Value Stream Elements:** Generate a complete list of all `ValueStream` elements (L0, L1, and L2) created in Step 2 and Step 3, including their Parent ID. This canonical list is the definitive source for all `ValueStream` records in the final `elements.csv`.
   3. **Consolidate All Business Objects:** Generate a complete list of all `BusinessObjects` (L0, L1, and L2) created in Step 5, including their Parent ID. This canonical list is the definitive source for all `BusinessObject` records in the final `elements.csv`.

### Step 4: Build the Value Stream Hierarchy (Mirroring the Anchor)

For each L0 `ValueStream`, you will now group its L2 stages into L1 stages. This grouping must **exactly mirror** the capability hierarchy.

**Procedure:**

1. For each relevant L1 `Capability`, create a corresponding L1 `ValueStream` stage within the L0 `ValueStream`.
   * The L2 stages under this new L1 stage are precisely those whose primary `Capability` is part of that L1 `Capability` group.
   * The name of each L1 stage must reflect a value-creating activity from the customer's perspective, inspired by its corresponding L1 `Capability` within the context of the L0 `ValueStream`.

### Step 5: Identify and Structure Business Objects (Mirroring the Anchor)

1. **Identify L2 Objects:** For each L2 `Capability`, identify its primary L2 `BusinessObject` it transforms (and has custodianship over).
   * **Valuable Entity Rule:** You must name the actual, valuable entity in the real world (e.g., `Customer Relationship` or `Customer`), not the information *about* it (e.g., `Customer Record`). Focus on business reality, not IT.
2. **Build the Object Hierarchy:** Create an L0/L1 `BusinessObject` hierarchy that **exactly mirrors** the `Capability` hierarchy.
   * An L1 `BusinessObject` must contain the exact same set of L2 `BusinessObjects` whose corresponding L2 `Capabilities` belong to the same L1 `Capability`.
   * Name L0/L1 objects as conceptual, singular nouns (e.g., `Customer Engagement`, `Product Portfolio`).

### Step 6: Formalize All Relationships for Output

1. **Define Base Relationships (L2):** Based on the previous steps, define all L2 relationships:
   * `AssociationRelationship`: From an L2 `Capability` to the L2 `BusinessObject` it transforms (from Step 5.1).
   * `ServingRelationship` (Manifestation): From an L2 `Capability` to the L2 `ValueStream` stage it manifests (from Step 3.3).
   * `ServingRelationship` (Support): From a provider L2 `Capability` to a consumer L2 `Capability` (from Steps 3.4 and 3.5).
2. **Define Composition Relationships:** Formally define all parent-child links in the three hierarchies (`Capability`, `BusinessObject`, `ValueStream`) by creating `CompositionRelationship`s.
3. **Derive L1 Relationships:** Based on step 6.1, derive all L2 relationships:
   * `AssociationRelationship`: For each `AssociationRelationship` from an L2 `Capability` to an L2 `BusinessObject`, create a corresponding relationship between their L1 parents, provided the L1 relationship does not yet exist.
   * `ServingRelationship` (Manifestation): For each `ServingRelationship` from an L2 `Capability` to the L2 `ValueStream`, create a corresponding relationship between their L1 parents, provided the L1 relationship does not yet exist.
   * `ServingRelationship` (Support): For each `ServingRelationship` from a provider L2 `Capability` to a consumer L2 `Capability`, create a corresponding relationship between their L1 parents, provided those parents are distinct and the L1 relationship does not yet exist.
4. **Create L0 Relationships:** Create an `AssociationRelationship` from the single L0 `Capability` to the single L0 `BusinessObject` and `ServingRelationships` to all L0 `ValueStreams`.
5. **Explicitly Present All Derived Relationships (Mandatory Checkpoint):**
   To ensure upward coherence, you must now explicitly list the complete, unique set of all non-composition L1 relationships created in Steps 6.3.

## Part 3: Output Specifications

**Instruction:** Your response must now consist of ONLY the three requested CSV code blocks. DO NOT include any further text, headers, or explanations outside of the code blocks themselves.

Generate the output as three separate code blocks for `elements.csv`, `relations.csv`, and `properties.csv`. The format must be standard CSV with headers, comma separators, and all text values in double quotes.

**1. `elements.csv` Table**

| Column          | Content                                                                      |
| :-------------- | :--------------------------------------------------------------------------- |
| `ID`            | A unique identifier for the element.                                         |
| `Type`          | The element type. **Use only:** `ValueStream`, `Capability`, `BusinessObject`. |
| `Name`          | The human-readable name of the element.                                      |
| `Documentation` | Leave empty.                                                                 |

**2. `relations.csv` Table**

| Column           | Content                                                                                      |
| :--------------- | :------------------------------------------------------------------------------------------- |
| `ID`             | Leave empty.                                                                                 |
| `Type`           | The ArchiMate relationship type. **Use only:** `CompositionRelationship`, `ServingRelationship`, `AssociationRelationship`. |
| `Name`           | Leave empty.                                                                                 |
| `Documentation`  | Leave empty.                                                                                 |
| `Source`         | The `ID` of the source element.                                                              |
| `Target`         | The `ID` of the target element.                                                              |
| `Specialization` | Leave empty.                                                                                 |

### Usage Rules for Relationship Types

To ensure correctness, you **must** adhere to the following rules when creating relations. No other combinations are permitted.

* **`CompositionRelationship`**: Used exclusively for parent-child relationships within the same hierarchy.
  * Source Type: `Capability`, Target Type: `Capability`
  * Source Type: `ValueStream`, Target Type: `ValueStream`
  * Source Type: `BusinessObject`, Target Type: `BusinessObject`

* **`ServingRelationship`**: Used for two specific purposes.
  * Source Type: `Capability`, Target Type: `ValueStream`
  * Source Type: `Capability`, Target Type: `Capability`

* **`AssociationRelationship`**: Used exclusively to relate capabilities to business objects.
  * Source Type: `Capability`, Target Type: `BusinessObject`

**3. `properties.csv` Table and Rules**

The `properties.csv` file must contain `"ID", "Key", "Value"`. Apply the following rules rigorously:

* **Rule 1 (All Elements):** Every single element from `elements.csv` must have these two properties:
  * A property with `Key` = "Level" and `Value` = the element's hierarchy level (starting at `0`).
* **Rule 2 (L0 ValueStreams):** Every top-level `ValueStream` element must have these **additional** properties:
  * A property with `Key` = "Value Proposition" and `Value` = the full description of the originating Value Proposition.
  * A property with `Key` = "Value Stream Pattern" and `Value` = the chosen value stream pattern (`MTS`, `ATO`, or `ETO`).

```
