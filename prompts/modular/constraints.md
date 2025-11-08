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
