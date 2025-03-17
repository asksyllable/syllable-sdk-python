---
title: 'SessionMessage'
---


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `role`                                                               | [models.DialogRole](../models/dialogrole.md)                         | TRUE                                                   | N/A                                                                  |
| `dialog`                                                             | [models.DialogMessage](../models/dialogmessage.md)                   | TRUE                                                   | N/A                                                                  |
| `tool_calls`                                                         | List[[models.DialogToolCall](../models/dialogtoolcall.md)]           | TRUE                                                   | N/A                                                                  |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | TRUE                                                   | N/A                                                                  |