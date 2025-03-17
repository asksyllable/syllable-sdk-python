---
title: 'CustomMessageRule'
---

## Example Usage

```typescript
import { CustomMessageRule } from "syllable-sdk/models/components";

let value: CustomMessageRule = {
  description: "justly pfft oh delete",
  timeRangeStart: "09:00",
  timeRangeEnd: "17:00",
  date: "2025-01-01",
  daysOfWeek: [
    "mo",
    "tu",
    "we",
    "th",
    "fr",
  ],
  invert: false,
  text: "Sorry, we're closed today",
};
```

## Fields

| Field                                                                                                 | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `description`                                                                                         | *string*                                                                                              | TRUE                                                                                    | The description of the rule                                                                           |                                                                                                       |
| `timeRangeStart`                                                                                      | *string*                                                                                              | FALSE                                                                                    | The start of the time range for the rule in 24-hour format hh:mm (should be null for "all day" cases) | 09:00                                                                                                 |
| `timeRangeEnd`                                                                                        | *string*                                                                                              | FALSE                                                                                    | The end of the time range for the rule in 24-hour format hh:mm (should be null for "all day" cases)   | 17:00                                                                                                 |
| `date`                                                                                                | *string*                                                                                              | FALSE                                                                                    | The date for the rule in YYYY-MM-DD format                                                            | 2025-01-01                                                                                            |
| `daysOfWeek`                                                                                          | [components.DayOfWeek](/sdk-docs/models/components/dayofweek)[]                                        | FALSE                                                                                    | The days of the week for the rule                                                                     | [<br/>"mo",<br/>"tu",<br/>"we",<br/>"th",<br/>"fr"<br/>]                                              |
| `invert`                                                                                              | *boolean*                                                                                             | TRUE                                                                                    | Whether the rule logic should be inverted (i.e. "not")                                                |                                                                                                       |
| `text`                                                                                                | *string*                                                                                              | TRUE                                                                                    | Message text associated with the rule                                                                 | Sorry, we're closed today                                                                             |