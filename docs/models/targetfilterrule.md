# TargetFilterRule

A single predicate over one enrichment attribute of an outbound request.

``field`` names a key in the request's enrichment payload (e.g. ``line_type``, ``carrier_name``,
``mcc``, ``mnc``). Any attribute captured at lookup time can be filtered on with no code change.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `field`                                                                         | *str*                                                                           | :heavy_check_mark:                                                              | Enrichment attribute to match on (a key in the request enrichment payload).     | **Example 1:** line_type<br/>**Example 2:** carrier_name<br/>**Example 3:** mnc |
| `op`                                                                            | [models.FilterOp](../models/filterop.md)                                        | :heavy_check_mark:                                                              | Comparison operator for a single target-filter rule.                            |                                                                                 |
| `values`                                                                        | List[*str*]                                                                     | :heavy_minus_sign:                                                              | Values to compare against. Ignored for exists / not_exists.                     | [<br/>"landline",<br/>"fixedVoip",<br/>"nonFixedVoip"<br/>]                     |