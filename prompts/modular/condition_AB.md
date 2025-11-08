<!-- INSERT HEADER.MD -->

## Part 2: Modeling Procedure

### Step 1: The Goal and Guiding Principles

Your primary goal is to create a coherent architectural model for the core business domain of the specified sector.

1. **Principle of Reusability:** You must develop a single, canonical set of reusable capabilities.
2. **Principle of Grounding:** After developing the core architecture, you will ground it by mapping it to the value streams defined in Part 1 to ensure nothing is missing.

<!-- FOR CONDITION B: INSERT CONSTRAINTS.MD -->

### Step 2: Develop Capability and Object Catalogs

1. **Develop the Business Capability Catalog:** Develop a detailed but consolidated and reusable set of `Capabilities` for the sector. Structure these into a logical hierarchy.
   * **Core Domain Mandate:** You **must** focus exclusively on **core** capabilities that are intrinsic to the sector's **primary value creation**. Strictly avoid defining generic, cross-sector administrative capabilities, even if they seem necessary. This includes, but is not limited to, capabilities for managing general IT systems, human resources, legal affairs, or financial accounting.
2. **Develop the Object Catalog:** Define a detailed but consolidated and reusable set of `BusinessObject`, again focusing on the core domain of the sector. Structure these into a hierarchy.

### Step 3: Develop the L0 Value Streams

<!-- INSERT VALUESTREAMS.MD -->

### Step 4: Decompose and Map Architecture to Value Streams

1. **Decompose Value Streams:** Decompose the top-level `ValueStreams` into stages.
2. **Define Mappings:** Map the `Capabilities` to the `ValueStream` stages that manifest them, and to the `BusinessObjects` they have custodianship over. Define support relationships between capabilities as needed.

### Step 4: Prepare for Final Output

1. Consolidate all final elements and relationships.
2. Assign a `Level` property to all elements based on their position in their respective hierarchies (top-level elements are Level 0, their children are Level 1, and so on).
3. Assign a `Sequence` property to the decomposed `ValueStream` elements.

<!-- INSERT FOOTER.MD -->
