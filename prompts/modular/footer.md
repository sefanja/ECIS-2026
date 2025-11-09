## Part 3: Output Specifications

**Instruction:** Your response must now consist of ONLY the three requested CSV code blocks. DO NOT include any further text, headers, or explanations outside of the code blocks themselves.

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
