---
title: 'DaoCustomMessageRule'
---

## Example Usage

```typescript
import { DaoCustomMessageRule } from "syllable-sdk/models/components";

let value: DaoCustomMessageRule = {
  description: "runny rough agreeable beneath unlike vastly but",
  invert: false,
  text: "<value>",
};
```

## Fields

| Field                                                                                                 | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `description`                                                                                         | *string*                                                                                              | TRUE                                                                                    | The description of the rule                                                                           |
| `timeRangeStart`                                                                                      | *string*                                                                                              | FALSE                                                                                    | The start of the time range for the rule in 24-hour format hh:mm (should be null for "all day" cases) |
| `timeRangeEnd`                                                                                        | *string*                                                                                              | FALSE                                                                                    | The end of the time range for the rule in 24-hour format hh:mm (should be null for "all day" cases)   |
| `date`                                                                                                | *string*                                                                                              | FALSE                                                                                    | The date for the rule in YYYY-MM-DD format                                                            |
| `daysOfWeek`                                                                                          | [components.DayOfWeek](/sdk-docs/models/components/dayofweek)[]                                        | FALSE                                                                                    | The days of the week for the rule                                                                     |
| `invert`                                                                                              | *boolean*                                                                                             | TRUE                                                                                    | Whether the rule logic should be inverted (i.e. "not")                                                |
| `text`                                                                                                | *string*                                                                                              | TRUE                                                                                    | Message text associated with the rule                                                                 |