---
title: 'Channel'
---

## Example Usage

```typescript
import { Channel } from "syllable-sdk/models/components";

let value: Channel = {
  name: "<value>",
  channelService: "webchat",
  supportedModes: "[\"chat\",\"voice\"]",
  id: 765326,
};
```

## Fields

| Field                                                                                                                                                 | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           | Example                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                | *string*                                                                                                                                              | TRUE                                                                                                                                    | The channel name                                                                                                                                      |                                                                                                                                                       |
| `channelService`                                                                                                                                      | [components.ChannelServices](/sdk-docs/models/components/channelservices)                                                                              | TRUE                                                                                                                                    | The communication service for a channel.                                                                                                              |                                                                                                                                                       |
| `supportedModes`                                                                                                                                      | *string*                                                                                                                                              | FALSE                                                                                                                                    | The comma-delimited list of supported modes for the channel, which defines the       possible communication methods for channel targets linked to it. | [<br/>"chat",<br/>"voice"<br/>]                                                                                                                       |
| `id`                                                                                                                                                  | *number*                                                                                                                                              | TRUE                                                                                                                                    | The channel ID                                                                                                                                        |                                                                                                                                                       |