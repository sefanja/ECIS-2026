<!-- INSERT HEADER.MD -->

## Part 2: Modeling Procedure

### Step 1: The Goal and Guiding Principles

Your primary goal is to create a coherent architectural model for the core business domain of the specified sector.

1. **Principle of Reusability:** You must develop a single, canonical set of capabilities that can be reused for multiple value streams.
2. **Principle of Grounding:** After developing the core architecture, you will ground it by mapping it to the value streams defined in Part 1 to ensure nothing is missing.

<!-- CONDITION B: INSERT CONSTRAINTS.MD -->

### Step 2: Develop Capability and Object Catalogs

1. **Develop the Business Capability Catalog:** Develop a highly detailed set of `Capabilities` for the sector. Structure these into a logical hierarchy.
   * **Core Domain Mandate:** You **must** focus exclusively on **core** capabilities that are intrinsic to the sector's **primary value creation**. Strictly avoid defining generic, cross-sector administrative capabilities, even if they seem necessary. This includes, but is not limited to, capabilities for managing general IT systems, human resources, legal affairs, or financial accounting.
2. **Develop the Object Catalog:** Define a highly detailed set of `BusinessObject`, again focusing on the core domain of the sector. Structure these into a hierarchy.

### Step 3: Develop the L0 Value Streams

<!-- INSERT VALUESTREAMS.MD -->

### Step 4: Decompose and Map Architecture to Value Streams

1. **Develop Value Stream Catalog:** Decompose the top-level `ValueStreams` into stages. Determine the number of stages required to narrate the complete and highly granular value creation process.
2. **Define Architectural Mappings:** Create mappings between the elements from the catalogs to show how they relate to each other:
   * Map `ValueStreams` (and stages) to the `Capabilities` that realize them.
   * Map `Capabilities` to the `BusinessObjects` they modify.
   <!-- CONDITION B: * Define support relationships between `Capabilities` to ensure all capabilities have a purpose. -->

### Step 5: Prepare for Final Output

1. Consolidate all final elements and relationships.
2. Assign a `Level` property to all elements based on their position in their respective hierarchies (top-level elements are Level 0, their children are Level 1, and so on).
3. Assign a `Sequence` property to the decomposed `ValueStream` elements.

<!-- INSERT FOOTER.MD -->
