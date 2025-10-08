# PronunciationOverridesDictionary

Container for all TTS pronunciation overrides belonging to the sub-organisation.

Stored in the `config_values` table via ConfigDao. The Syllable API persists uploaded CSV
pronunciation rules, and Bubblegum's PronunciationOverridesPlugin reads them to apply text
replacements before TTS processing.

Example:
    dao = ConfigDao(db_session)
    await dao.register_model('tts.pronunciations', PronunciationOverridesDictionary)

    pod = PronunciationOverridesDictionary(
        pronunciations=[...],
        metadata=DictionaryMetadata(entries=10, hash='sha256:...'),
    )
    result = await dao.upsert('pronunciations_v1', pod)

    record = await dao.get('pronunciations_v1', PronunciationOverridesDictionary)
    if record:
        pronunciations = record.value.pronunciations


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `type`                                                                   | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | N/A                                                                      |
| `pronunciations`                                                         | List[[models.PronunciationOverride](../models/pronunciationoverride.md)] | :heavy_check_mark:                                                       | N/A                                                                      |
| `voices`                                                                 | Dict[str, [models.VoiceDisplayInfo](../models/voicedisplayinfo.md)]      | :heavy_minus_sign:                                                       | N/A                                                                      |
| `metadata`                                                               | [models.DictionaryMetadata](../models/dictionarymetadata.md)             | :heavy_check_mark:                                                       | Audit metadata associated with a dictionary.                             |