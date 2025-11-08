# Reference Architecture Design Brief

## Part 1: Context & Scope

You are an experienced business architect tasked with creating a business architecture reference model for a particular sector. To ground the model in strategic purpose, your first task is to create a concise yet complete Sector Context Profile.

### Sector Context Profile

**Sector to be Analyzed:** Research-Intensive Universities

* **Core Purpose & Societal Role:** Describe the sector's fundamental purpose. Why does it exist? What societal need does it fulfill?
* **Primary Business Model Archetype(s):** Identify the dominant business model. Think in terms of B2C (to consumers), B2B (to businesses), B2G (to government), or non-profit/public funding. A hybrid model is possible.
* **Key Strategic Drivers & Basis of Competition:** On what basis do organizations in this sector compete? Consider factors like reputation, innovation, efficiency, customer satisfaction, or societal impact. Name the 2-3 most important ones.
* **Dominant Environmental Factors:** Describe the context in which the sector operates. Consider laws and regulations, public accountability, technological trends, or funding models (e.g., public funds).

### Strategic Foundation

1. Identify **2-3 primary, external `Customer Segments`** for the defined sector.
2. For **each** `Customer Segment`, describe the core `Value Proposition` it receives from the organization. Focus on the ultimate value for the customer.
3. Present the result as a list where each `Customer Segment` is paired with its `Value Proposition(s)`.

## Part 2: Modeling Procedure

### Step 1: The Goal and Guiding Principles

Your primary goal is to create a coherent architectural model for the core business domain of the specified sector.

1. **Principle of Reusability:** You must develop a single, canonical set of reusable capabilities.
2. **Principle of Grounding:** After developing the core architecture, you will ground it by mapping it to the value streams defined in Part 1 to ensure nothing is missing.

### Step 2: Develop Capability and Object Catalogs

1. **Develop the Business Capability Catalog:** Develop a detailed but consolidated and reusable set of `Capabilities` for the sector. Structure these into a logical hierarchy.
   * **Core Domain Mandate:** You **must** focus exclusively on **core** capabilities that are intrinsic to the sector's **primary value creation**. Strictly avoid defining generic, cross-sector administrative capabilities, even if they seem necessary. This includes, but is not limited to, capabilities for managing general IT systems, human resources, legal affairs, or financial accounting.
2. **Develop the Object Catalog:** Define a detailed but consolidated and reusable set of `BusinessObject`, again focusing on the core domain of the sector. Structure these into a hierarchy.

### Step 3: Develop the L0 Value Streams

1. **Define L0 Value Streams using CODP:** Based on the customer segments and their value propositions identified eralier, define the complete set of L0 `ValueStreams`.
   * **Principle:** If the organization creates a standardized, reusable business asset 'to stock' (**Make-to-Stock, MTS**), this is a separate L0 `ValueStream`. The flow triggered by a customer order (**Assemble-to-Order, ATO**) is another.
   * **Litmus Test:** Ask "Does the organization build a core asset *before* any specific customer is known?"
     * **Example:** A software company develops a standard `Platform` (MTS) before a client signs up. Configuring that platform for a new client (ATO) is a separate L0 Value Stream.
   * **Action:** Use this logic to define all internal asset-creation streams (MTS) and all customer-facing delivery streams (ATO/ETO).
2. **Characterize All Value Streams:** For every L0 `ValueStream` defined above:
    * Assign a `Value Stream Pattern (CODP)`: Choose one of `ETO`, `ATO`, or `MTS`.
    * Use the 'deepest' pattern (`ETO` > `ATO` > `MTS`) that represents a typical case for the sector.
3. Present the result as a list: `[L0 Value Stream Name, Description, Originating VP, Value Stream Pattern]`.

### Step 4: Decompose and Map Architecture to Value Streams

1. **Decompose Value Streams:** Decompose the top-level `ValueStreams` into stages.
2. **Define Mappings:** Map the `Capabilities` to the `ValueStream` stages that manifest them, and to the `BusinessObjects` they have custodianship over. Define support relationships between capabilities as needed.

### Step 4: Prepare for Final Output

1. Consolidate all final elements and relationships.
2. Assign a `Level` property to all elements based on their position in their respective hierarchies (top-level elements are Level 0, their children are Level 1, and so on).
3. Assign a `Sequence` property to the decomposed `ValueStream` elements.

## Part 3: Output Specifications

Generate the output as three separate code blocks for `elements.csv`, `relations.csv`, and `properties.csv`. The format must be standard CSV with headers, comma separators, and all text values in double quotes.

**1. `elements.csv` Table**

| Column          | Content                                                                      |
| :-------------- | :--------------------------------------------------------------------------- |
| `ID`            | A unique identifier for the element.                                         |
| `Type`          | The element type. **Use only:** `ValueStream`, `Capability`, `BusinessObject`. |
| `Name`          | The human-readable name of the element.                                      |
| `Documentation` | A concise description of the element's purpose.                              |

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
  * Use 1 (Manifestation): To show that a capability is manifested as value stream (stage).
    * Source Type: `Capability`, Target Type: `ValueStream`
  * Use 2 (Support): To show that one capability provides support to another.
    * Source Type: `Capability`, Target Type: `Capability`

* **`AssociationRelationship`**: Used exclusively to show that a capability has custodianship over a business object.
  * Source Type: `Capability`, Target Type: `BusinessObject`

**3. `properties.csv` Table and Rules**

The `properties.csv` file must contain `"ID", "Key", "Value"`. Apply the following rules rigorously:

* **Rule 1 (All Elements):** Every single element from `elements.csv` must have these two properties:
  * A property with `Key` = "Level" and `Value` = the element's hierarchy level (`0`, `1`, or `2`).
* **Rule 2 (L0 ValueStreams):** Every L0 `ValueStream` element must have these **additional** properties:
  * A property with `Key` = "Value Proposition" and `Value` = the full description of the originating Value Proposition.
  * A property with `Key` = "Value Stream Pattern" and `Value` = the chosen value (`MTS`, `ATO`, or `ETO`).
* **Rule 3 (L2 ValueStreams):** Every L2 `ValueStream` element must have one **additional** property:
  * A property with `Key` = "Sequence" and `Value` = a number indicating its sequential position within its parent L0 `ValueStream` (starting from "1" for each stream).
