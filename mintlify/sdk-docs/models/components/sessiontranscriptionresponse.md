---
title: 'SessionTranscriptionResponse'
---

Text transcript of a given session. For more information, see
[Console docs](https://docs.syllable.ai/workspaces/Sessions).

## Example Usage

```typescript
import { SessionTranscriptionResponse } from "syllable-sdk/models/components";

let value: SessionTranscriptionResponse = {
  sessionId: "<id>",
  transcription: [
    {
      timestamp: new Date("2025-01-02T08:48:44.316Z"),
      lang: "en-US",
      source: "user",
    },
  ],
  actions: [
    {
      timestamp: new Date("2024-03-13T13:08:44.087Z"),
    },
  ],
};
```

## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `sessionId`                                                            | *string*                                                               | TRUE                                                     | Internal ID of the session                                             |
| `transcription`                                                        | [components.SessionText](/sdk-docs/models/components/sessiontext)[]     | TRUE                                                     | Transcriptions of all messages in the session                          |
| `actions`                                                              | [components.SessionAction](/sdk-docs/models/components/sessionaction)[] | TRUE                                                     | Tool invocations that occurred during the session                      |