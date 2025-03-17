---
title: 'CustomMessageCreateRequest'
---

## Example Usage

```typescript
import { CustomMessageCreateRequest } from "syllable-sdk/models/components";

let value: CustomMessageCreateRequest = {
  name: "<value>",
  text: "<value>",
  rules: [
    {
      description: "given brochure hence hence per formal aw cutover",
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
    },
  ],
};
```

## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `name`                                                                         | *string*                                                                       | TRUE                                                             | The name of the custom message                                                 |
| `text`                                                                         | *string*                                                                       | TRUE                                                             | The text of the custom message                                                 |
| `label`                                                                        | *string*                                                                       | FALSE                                                             | The label of the custom message                                                |
| `rules`                                                                        | [components.CustomMessageRule](/sdk-docs/models/components/custommessagerule)[] | FALSE                                                             | Rules for time-specific message variants                                       |
| `type`                                                                         | *string*                                                                       | FALSE                                                             | N/A                                                                            |