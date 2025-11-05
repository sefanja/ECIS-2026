<!-- INSERT HEADER.MD -->

### Step 6: Formalize All Relationships for Output

1. **Define Base Relationships (L2):** Based on the previous steps, define all L2 relationships:
   * `AssociationRelationship`: From an L2 `Capability` to the L2 `BusinessObject` it has custodianship over (from Step 5.1).
   * `ServingRelationship` (Manifestation): From an L2 `Capability` to the L2 `ValueStream` stage it manifests (from Step 1.2).
   * `ServingRelationship` (Support): From a provider L2 `Capability` to a consumer L2 `Capability` (from Step 2).
2. **Define Composition Relationships:** Formally define all parent-child links in the three hierarchies (`Capability`, `BusinessObject`, `ValueStream`) by creating `CompositionRelationship`s.
3. **Construct All Aggregate Relationships:** You will now construct the complete set of L1 and L0 relationships. **Do not invent any new relationships.** The higher-level relationships are created *exclusively* by applying the following mechanical procedure:
   * **Phase A: Construct L1 Relationships.**
     * Start with an empty set of L1 relationships.
       * For **every L2 relationship** you defined in Step 6.1, identify the L1 parent of its source and the L1 parent of its target.
       * If these L1 parents are not the same element, add a corresponding relationship of the same type to your set of L1 relationships. Avoid adding duplicates.
     * **Phase B: Construct L0 Relationships.**
       * Start with an empty set of L0 relationships.
       * For **every L1 relationship** in the set you just constructed in Phase A, identify the L0 parent of its source and the L0 parent of its target.
       * If these L0 parents are not the same element, add a corresponding relationship of the same type to your set of L0 relationships. Avoid adding duplicates.
4. **Mandatory Verification:** Prove you have applied the derivation rule correctly by providing one concrete example for **each** of the three main relationship patterns.
   * **A. Capability Support:** Select one L2 `ServingRelationship` from a provider capability to a consumer capability. State the L1 parents of both, and then state the derived L1 `ServingRelationship` that must exist.
   * **B. Capability-Object:** Select one L2 `AssociationRelationship`. State the L1 parents of the source and target, and then state the derived L1 `AssociationRelationship` that must exist.
   * **C. Capability-ValueStream:** Select one L2 `ServingRelationship` from a capability to a value stream stage. State the L1 parents of both, and then state the derived L1 `ServingRelationship` that must exist.

## Part 2: Modeling Procedure

**Core Principle: Consistency by Construction**
This procedure is designed to construct a model that is coherent by design. Follow the steps precisely to build the different architectural views from a single, canonical capability model that serves as the "anchor".

**General Instruction on Brevity**
Throughout this entire procedure, do not add any conversational text, summaries, or explanations. Your response must consist only of the specific data deliverables requested in each step.

You will now apply this procedure to create the detailed architectural model for the previously defined sector: **Research-Intensive Universities**.

### Step 1: Discover Capabilities and Value Stream Stages Iteratively

You will now analyze each L0 `ValueStream` one by one to discover the complete set of capabilities.

**Procedure:**
Execute the following process for each L0 `ValueStream` identified in Part 1. You **must** process the `MTS` (Make-to-Stock) streams first before processing any `ATO` (Assemble-to-Order) or `ETO` (Engineer-to-Order) streams. This ensures that foundational, reusable capabilities are discovered first.

For each L0 `ValueStream`:

1. **Deconstruct into Stages:** Deconstruct the L0 `ValueStream` into a logical sequence of stages. Choose a number of stages that is sufficient to tell the core but detailed value creation story, focusing on significant milestones.
2. **Ensure Lifecycle Completeness:** For an `ATO` or `ETO` stream, verify that the sequence of stages covers the following logical phases. If not, add the necessary stages:
   * **Engagement & Acquisition:** Initial contact, qualification, and agreement.
     * **Core Value Delivery:** The central activities the customer is paying for.
     * **Counter-Performance:** Securing the reciprocal value (e.g., `Process Payment`, `Collect Fee`).
     * **After-Care & Support:** Post-delivery support and issue resolution.
3. **Identify Primary Capabilities:** For each L2 `ValueStream` stage, identify the primary L2 `Capability` it manifests. Adhere to the following rules:
   * **Naming Convention:** Adhere to the **Verb-Plural Noun** format (e.g., `Assess Customer Needs`, `Develop New Products`).
   * **Granularity Rule:** The capability must be generic enough to be potentially reusable in other contexts, but specific enough that it manifests as only **one** L2 stage within the same L0 value stream.
     * **Litmus Test:** If you are tempted to assign the same capability to multiple stages of the same L0 value stream (e.g., assigning `Manage Service Requests` to both "Receive Request" and "Fulfill Request"), your capability is too broad. You must define more granular capabilities instead (e.g., `Process Intake Requests` and `Deliver Services`).
4. **Discover Supporting Capabilities (First Level):** For each primary L2 `Capability` you just identified, list its 1-3 most critical, direct supporting L2 `Capabilities` (or a justified 0). Adhere to the **naming convention** and the following rules:
   * **Reuse First:** Before defining a new capability, **always check if a suitable one has already been discovered** in a previous step or value stream. A primary capability in one value stream can be reused as supporting in another.
   * **The Value-Flow Direction Rule:** Support flows from foundational to operational capabilities.
   * **Core Domain Mandate:** You **must** focus exclusively on core capabilities. Strictly avoid generic administrative capabilities (IT, HR, Legal, Finance).
5. **Discover Deeper Supporting Capabilities (Second Level):** Now, for each **newly discovered supporting capability** from the previous step, repeat the process: identify its 1-2 most critical supporting L2 `Capabilities` (or a justified 0), adhering to the **naming convention**, **reuse first**, **value-flow direction**, and **core domain mandate** mentioned above.

### Step 2: Build the Canonical Capability Hierarchy (The ANCHOR)

1. Combine all unique L2 `Capabilities` discovered in Step 1 into a single, canonical list.
2. Group these L2 `Capabilities` under a set of L1 `Capabilities`.
   * **Crucial Rule for Coherence:** Each L2 `Capability` must be assigned to **exactly one** L1 `Capability` parent.
   * **Naming Convention:** Use a **Verb-Plural Noun** format to describe the potential value creating behavior (e.g., `Assess Customer Needs`, `Develop New Products`).
3. Group all L1 `Capabilities` under a single L0 `Capability`, using the same **naming convention**.

### Step 3: Build the Value Stream Hierarchy (Mirroring the Anchor)

For each L0 `ValueStream`, you will now group its L2 stages into L1 stages. This grouping must **exactly mirror** the capability hierarchy.

**Procedure:**

1. For each relevant L1 `Capability`, create a corresponding L1 `ValueStream` stage within the L0 `ValueStream`.
   * The L2 stages under this new L1 stage are precisely those whose primary `Capability` is part of that L1 `Capability` group.
   * The name of each L1 stage must reflect a value-creating activity from the customer's perspective, inspired by its corresponding L1 `Capability` within the context of the L0 `ValueStream`.

### Step 4: Identify and Structure Business Objects (Mirroring the Anchor)

1. **Identify L2 Objects:** For each L2 `Capability`, identify its primary L2 `BusinessObject` it has custodianship over.
   * **Valuable Entity Rule:** You must name the actual, valuable entity in the real world (e.g., `Customer Relationship` or `Customer`), not the information *about* it (e.g., `Customer Record`). Focus on business reality, not IT.
2. **Build the Object Hierarchy:** Create an L0/L1 `BusinessObject` hierarchy that **exactly mirrors** the `Capability` hierarchy.
   * An L1 `BusinessObject` must contain the exact same set of L2 `BusinessObjects` whose corresponding L2 `Capabilities` belong to the same L1 `Capability`.
   * Name L0/L1 objects as conceptual, singular nouns (e.g., `Customer Engagement`, `Product Portfolio`).

### Step 5: Formalize All Relationships for Output

1. **Define Base Relationships (L2):** Based on the previous steps, define all L2 relationships:
   * `AssociationRelationship`: From an L2 `Capability` to the L2 `BusinessObject` it has custodianship over (from Step 4.1).
   * `ServingRelationship` (Manifestation): From an L2 `Capability` to the L2 `ValueStream` stage it manifests (from Step 1.3).
   * `ServingRelationship` (Support): From a provider L2 `Capability` to a consumer L2 `Capability` (from Steps 1.4 and 1.5).
2. **Define Composition Relationships:** Formally define all parent-child links in the three hierarchies (`Capability`, `BusinessObject`, `ValueStream`) by creating `CompositionRelationship`s.
3. **Construct All Aggregate Relationships:** You will now construct the complete set of L1 and L0 relationships. **Do not invent any new relationships.** The higher-level relationships are created *exclusively* by applying the following mechanical procedure:
   * **Phase A: Construct L1 Relationships.**
     * Start with an empty set of L1 relationships.
       * For **every L2 relationship** you defined in Step 5.1, identify the L1 parent of its source and the L1 parent of its target.
       * If these L1 parents are not the same element, add a corresponding relationship of the same type to your set of L1 relationships. Avoid adding duplicates.
     * **Phase B: Construct L0 Relationships.**
       * Start with an empty set of L0 relationships.
       * For **every L1 relationship** in the set you just constructed in Phase A, identify the L0 parent of its source and the L0 parent of its target.
       * If these L0 parents are not the same element, add a corresponding relationship of the same type to your set of L0 relationships. Avoid adding duplicates.
4. **Mandatory Verification:** Prove you have applied the derivation rule correctly by providing one concrete example for **each** of the three main relationship patterns.
   * **A. Capability Support:** Select one L2 `ServingRelationship` from a provider capability to a consumer capability. State the L1 parents of both, and then state the derived L1 `ServingRelationship` that must exist.
   * **B. Capability-Object:** Select one L2 `AssociationRelationship`. State the L1 parents of the source and target, and then state the derived L1 `AssociationRelationship` that must exist.
   * **C. Capability-ValueStream:** Select one L2 `ServingRelationship` from a capability to a value stream stage. State the L1 parents of both, and then state the derived L1 `ServingRelationship` that must exist.

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

<!-- INSERT FOOTER.MD -->
