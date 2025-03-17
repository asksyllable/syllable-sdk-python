---
title: 'CustomMessageResponse'
---

A custom message is a pre-configured message delivered by an agent as a greeting at the
beginning of a conversation. Multiple agents can use the same custom mesasage. A custom message
has one or more rules defined, which allow for different messages to be dynamically selected and
delivered at runtime based on the current time and either date or day of the week. For more 
information, see [Console docs](https://docs.syllable.ai/Resources/Messages).

## Example Usage

```typescript
import { CustomMessageResponse } from "syllable-sdk/models/components";

let value: CustomMessageResponse = {
  name: "<value>",
  text: "<value>",
  rules: [
    {
      description: "advanced afterwards coliseum",
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
  id: 621479,
  updatedAt: new Date("2024-09-24T15:25:14.861Z"),
  lastUpdatedBy: "user@email.com",
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `name`                                                                                        | *string*                                                                                      | TRUE                                                                            | The name of the custom message                                                                |                                                                                               |
| `text`                                                                                        | *string*                                                                                      | TRUE                                                                            | The text of the custom message                                                                |                                                                                               |
| `label`                                                                                       | *string*                                                                                      | FALSE                                                                            | The label of the custom message                                                               |                                                                                               |
| `rules`                                                                                       | [components.CustomMessageRule](/sdk-docs/models/components/custommessagerule)[]                | FALSE                                                                            | Rules for time-specific message variants                                                      |                                                                                               |
| `id`                                                                                          | *number*                                                                                      | TRUE                                                                            | The ID of the custom message                                                                  |                                                                                               |
| `updatedAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | TRUE                                                                            | Timestamp of the most recent update to the custom message                                     |                                                                                               |
| `agentCount`                                                                                  | *number*                                                                                      | FALSE                                                                            | The number of agents using the custom message                                                 |                                                                                               |
| `lastUpdatedBy`                                                                               | *string*                                                                                      | TRUE                                                                            | The email address of the user who most recently updated the custom message                    | user@email.com                                                                                |
| `type`                                                                                        | *string*                                                                                      | FALSE                                                                            | N/A                                                                                           |                                                                                               |