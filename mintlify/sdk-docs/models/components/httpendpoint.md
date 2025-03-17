---
title: 'HttpEndpoint'
---

The configuration for an HTTP API call.

## Example Usage

```typescript
import { HttpEndpoint } from "syllable-sdk/models/components";

let value: HttpEndpoint = {
  url: "https://showy-tectonics.net",
  method: "post",
  argumentLocation: "form",
};
```

## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `url`                                                                      | *string*                                                                   | TRUE                                                         | The endpoint URL of the external service to call.                          |
| `method`                                                                   | [components.Method](/sdk-docs/models/components/method)                     | TRUE                                                         | The HTTP method to use for the service call.                               |
| `argumentLocation`                                                         | [components.ArgumentLocation](/sdk-docs/models/components/argumentlocation) | TRUE                                                         | How to pass the arguments to the request.                                  |