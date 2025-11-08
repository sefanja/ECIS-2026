<!-- INSERT HEADER.MD -->

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

### Step 2: Define the L0 Value Streams

<!-- INSERT VALUESTREAMS.MD -->

### Step 3: Discover L2 Capabilities and Value Stream Stages Iteratively

You will now analyze each L0 `ValueStream` one by one to discover the complete set of capabilities.

**Procedure:**
Execute the following process for each L0 `ValueStream`. You **must** process the `MTS` (Make-to-Stock) streams first before processing any `ATO` (Assemble-to-Order) or `ETO` (Engineer-to-Order) streams. This ensures that foundational, reusable capabilities are discovered first.

For each L0 `ValueStream`:

1. **Deconstruct into Stages:** Deconstruct the L0 `ValueStream` into a logical sequence of stages. Choose a number of stages that is sufficient to tell the core but detailed value creation story, focusing on significant milestones. Asign a `Sequence` number to each L2 stage (starting from "1" for each L0 stream).
2. **Ensure Lifecycle Completeness:** For an `ATO` or `ETO` stream, verify that the sequence of stages covers the following logical phases. If not, add the necessary stages:
   * **Engagement & Acquisition:** Initial contact, qualification, and agreement.
     * **Core Value Delivery:** The central activities the customer is paying for.
     * **Counter-Performance:** Securing the reciprocal value (e.g., `Process Payment`, `Collect Fee`).
     * **After-Care & Support:** Post-delivery support and issue resolution.
3. **Identify Primary Capabilities:** For each L2 `ValueStream` stage, identify the primary L2 `Capability` it manifests. Adhere to the following rules:
   * **Naming Convention:** Adhere to the **Verb-Plural Noun** format (e.g., `Assess Customer Needs`, `Develop New Products`).
   * **Granularity Rule:** The capability must be generic enough to be potentially reusable in other contexts, but specific enough that it manifests as only **one** L2 stage within the same L0 value stream.
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

### Step 4: Build the Value Stream Hierarchy (Mirroring the Anchor)

For each L0 `ValueStream`, you will now group its L2 stages into L1 stages. This grouping must **exactly mirror** the capability hierarchy.

**Procedure:**

1. For each relevant L1 `Capability`, create a corresponding L1 `ValueStream` stage within the L0 `ValueStream`.
   * The L2 stages under this new L1 stage are precisely those whose primary `Capability` is part of that L1 `Capability` group.
   * The name of each L1 stage must reflect a value-creating activity from the customer's perspective, inspired by its corresponding L1 `Capability` within the context of the L0 `ValueStream`.

### Step 5: Identify and Structure Business Objects (Mirroring the Anchor)

1. **Identify L2 Objects:** For each L2 `Capability`, identify its primary L2 `BusinessObject` it has custodianship over.
   * **Valuable Entity Rule:** You must name the actual, valuable entity in the real world (e.g., `Customer Relationship` or `Customer`), not the information *about* it (e.g., `Customer Record`). Focus on business reality, not IT.
2. **Build the Object Hierarchy:** Create an L0/L1 `BusinessObject` hierarchy that **exactly mirrors** the `Capability` hierarchy.
   * An L1 `BusinessObject` must contain the exact same set of L2 `BusinessObjects` whose corresponding L2 `Capabilities` belong to the same L1 `Capability`.
   * Name L0/L1 objects as conceptual, singular nouns (e.g., `Customer Engagement`, `Product Portfolio`).

### Step 6: Formalize All Relationships for Output

1. **Define Base Relationships (L2):** Based on the previous steps, define all L2 relationships:
   * `AssociationRelationship`: From an L2 `Capability` to the L2 `BusinessObject` it has custodianship over (from Step 5.1).
   * `ServingRelationship` (Manifestation): From an L2 `Capability` to the L2 `ValueStream` stage it manifests (from Step 3.3).
   * `ServingRelationship` (Support): From a provider L2 `Capability` to a consumer L2 `Capability` (from Steps 3.4 and 3.5).
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
4. **Explicitly Present All Aggregated Relationships (Mandatory Checkpoint):**
   To ensure upward coherence, you must now explicitly list the complete, unique set of all aggregated non-composition relationships derived in Step 6.3 (Phases A and B). **These derived relationships must be included in the final `relations.csv` output.**
   1. **Present All L1 Derived Relationships:** A unique list of all derived L1 `ServingRelationship`s and L1 `AssociationRelationship`s.
   2. **Present All L0 Derived Relationships:** A unique list of all derived L0 `ServingRelationship`s and L0 `AssociationRelationship`s.
   *Your response must now contain this list before proceeding to Step 6.4.*
5. **Mandatory Verification:** Prove you have applied the derivation rule correctly by providing one concrete example for **each** of the three main relationship patterns.
   * **A. Capability Support:** Select one L2 `ServingRelationship` from a provider capability to a consumer capability. State the L1 parents of both, and then state the derived L1 `ServingRelationship` that must exist.
   * **B. Capability-Object:** Select one L2 `AssociationRelationship`. State the L1 parents of the source and target, and then state the derived L1 `AssociationRelationship` that must exist.
   * **C. Capability-ValueStream:** Select one L2 `ServingRelationship` from a capability to a value stream stage. State the L1 parents of both, and then state the derived L1 `ServingRelationship` that must exist.

<!-- INSERT FOOTER.MD -->