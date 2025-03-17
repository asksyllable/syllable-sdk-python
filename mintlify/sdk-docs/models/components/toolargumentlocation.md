---
title: 'ToolArgumentLocation'
---

The location of the argument in a tool HTTP request.
'body' is used for JSON data in the POST request body.
'form' is used for form data in the POST request body.
'path' is used for URL path parameters.
'query' is used for query parameters in the URL.

## Example Usage

```typescript
import { ToolArgumentLocation } from "syllable-sdk/models/components";

let value: ToolArgumentLocation = "body";
```

## Values

```typescript
"body" | "form" | "path" | "query"
```