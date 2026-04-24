# A2pMessagingPathCheckResponse

Twilio-side A2P setup state for the number.

Reflects Twilio configuration (Messaging Service + Brand + Campaign records); it is not
carrier per-number REGISTERED state or legal/content compliance.


## Fields

| Field                                                                                                                                                | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `a2p_approved`                                                                                                                                       | *bool*                                                                                                                                               | :heavy_check_mark:                                                                                                                                   | True when the number is on a Messaging Service with a US A2P registration whose brand is approved and campaign is verified on the same registration. |