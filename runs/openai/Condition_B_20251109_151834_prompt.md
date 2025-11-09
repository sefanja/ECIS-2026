# Prompt for Condition_B

```markdown
# Reference Architecture Design Brief

## Part 1: Context & Scope

You are an experienced business architect tasked with creating a business architecture reference model for a particular sector. To ground the model in strategic purpose, your first task is to create a concise yet complete Sector Context Profile.

### Sector Context Profile

**Sector to be Analyzed:** Research-Intensive Universities

* **Core Purpose & Societal Role:** Describe the sector's fundamental purpose. Why does it exist? What societal need does it fulfill?
* **Primary Business Model Archetype(s):** Identify the dominant business model. Think in terms of B2C (to consumers), B2B (to businesses), B2G (to government), or non-profit/public funding. A hybrid model is possible.
* **Key Strategic Drivers & Basis of Competition:** On what basis do organizations in this sector compete? Consider factors like reputation, innovation, efficiency, customer satisfaction, or societal impact. Name the 2-3 most important ones.
* **Dominant Environmental Factors:** Describe the context in which the sector operates. Consider laws and regulations, public accountability, technological trends, or funding models (e.g., public funds).

## Part 2: Modeling Procedure

### Step 1: The Goal and Guiding Principles

Your primary goal is to create a coherent architectural model for the core business domain of the specified sector.

1. **Principle of Reusability:** You must develop a single, canonical set of capabilities that can be reused for multiple value streams.
2. **Principle of Grounding:** After developing the core architecture, you will ground it by mapping it to the value streams defined in Part 1 to ensure nothing is missing.

#### Formal Modeling Constraints

The final model **must** adhere to the following nine formal constraints.

**Constraints for Consistent Zooming (C1-C5)**
This first set of constraints governs the hierarchical structures that enable consistent zooming across different levels of granularity. We refer to elements in these hierarchies as parents, children, and ancestors.

* **(C1) Unique parent:** Each element must have at most one parent.
* **(C2) Acyclicity:** An element cannot be its own ancestor.
* **(C3) Consistent refinement depth:** All leaf elements (elements without children) must have the same number of ancestors.
* **(C4) Upward coherence:** A non-hierarchical relationship between two elements requires a corresponding relationship between their parents (if any), provided the parents are distinct and with one exception: the relationship does not need to be propagated if the parent elements are both primary capabilities within the same top-level value stream.
* **(C5) Downward coherence:** A relationship between two parent elements requires that at least one pair of their respective children (if any) is also related.

**Constraints for Cross-Perspective Alignment (C6-C10)**
The second set of constraints ensures that the three perspectives remain aligned, forming a coherent triad. We treat value streams and stages as the same ontological type, referring to both as `ValueStreams`.

* **(C6) Capability impact:** Each business `Capability` must transform exactly one `BusinessObject`, with one exception: at the leaf level it may transform multiple objects.
* **(C7) Object relevance:** Each `BusinessObject` must be transformed by exactly one business `Capability`, with one exception: at the leaf level, an object may be transformed by multiple capabilities.
* **(C8) Capability purpose:** Each business `Capability` must either manifest as a primary capability in a `ValueStream` or support another capability that does.
* **(C9) Traceability:** Each `ValueStream` must manifest exactly one business `Capability`.
* **(C10) Exclusive manifestation:** Each `Capability` may manifest only once as primary per top-level `ValueStream`, with an exception for the leaf-level.

The leaf-level exceptions in rules C6, C7, and C10 may only be applied in exceptional cases and when justified.

### Step 2: Develop Capability and Object Catalogs

1. **Develop the Business Capability Catalog:** Develop a highly detailed set of `Capabilities` for the sector. Structure these into a logical hierarchy.
   * **Core Domain Mandate:** You **must** focus exclusively on **core** capabilities that are intrinsic to the sector's **primary value creation**. Strictly avoid defining generic, cross-sector administrative capabilities, even if they seem necessary. This includes, but is not limited to, capabilities for managing general IT systems, human resources, legal affairs, or financial accounting.
2. **Develop the Object Catalog:** Define a highly detailed set of `BusinessObject`, again focusing on the core domain of the sector. Structure these into a hierarchy.

### Step 3: Develop the L0 Value Streams

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

### Step 4: Decompose and Map Architecture to Value Streams

1. **Develop Value Stream Catalog:** Decompose the top-level `ValueStreams` into stages. Determine the number of stages required to narrate the complete and highly granular value creation process.
2. **Define Architectural Mappings:** Create mappings between the elements from the catalogs to show how they relate to each other:
   * Map `ValueStreams` (and stages) to the `Capabilities` that realize them.
   * Map `Capabilities` to the `BusinessObjects` they modify.
   * Define support relationships between `Capabilities` to ensure all capabilities have a purpose.

### Step 5: Prepare for Final Output

1. Consolidate all final elements and relationships.
2. Assign a `Level` property to all elements based on their position in their respective hierarchies (top-level elements are Level 0, their children are Level 1, and so on).
3. Assign a `Sequence` property to the decomposed `ValueStream` elements.

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
