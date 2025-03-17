---
title: 'SessionRecordingResponse'
---

Recording URLs for a given session.

## Example Usage

```typescript
import { SessionRecordingResponse } from "syllable-sdk/models/components";

let value: SessionRecordingResponse = {};
```

## Fields

| Field                          | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `sessionId`                    | *string*                       | FALSE             | The internal ID of the session |
| `recordings`                   | *string*[]                     | FALSE             | List of recording URLs         |