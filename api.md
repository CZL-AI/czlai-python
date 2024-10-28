# Aidoc

Types:

```python
from czlai.types import AidocIfContinueAskResponse, AidocIfNeedImageResponse
```

Methods:

- <code title="post /aidoc/if-continue-ask">client.aidoc.<a href="./src/czlai/resources/aidoc.py">if_continue_ask</a>(\*\*<a href="src/czlai/types/aidoc_if_continue_ask_params.py">params</a>) -> str</code>
- <code title="post /aidoc/if-need-image">client.aidoc.<a href="./src/czlai/resources/aidoc.py">if_need_image</a>(\*\*<a href="src/czlai/types/aidoc_if_need_image_params.py">params</a>) -> <a href="./src/czlai/types/aidoc_if_need_image_response.py">object</a></code>
- <code title="post /aidoc/pic-result">client.aidoc.<a href="./src/czlai/resources/aidoc.py">pic_result</a>(\*\*<a href="src/czlai/types/aidoc_pic_result_params.py">params</a>) -> None</code>
- <code title="post /aidoc/report">client.aidoc.<a href="./src/czlai/resources/aidoc.py">report</a>(\*\*<a href="src/czlai/types/aidoc_report_params.py">params</a>) -> None</code>
- <code title="post /aidoc/report-task">client.aidoc.<a href="./src/czlai/resources/aidoc.py">report_task</a>(\*\*<a href="src/czlai/types/aidoc_report_task_params.py">params</a>) -> None</code>

# AidocExotic

Types:

```python
from czlai.types import (
    AidocExoticAskContinueResponse,
    AidocExoticIfNeedImageResponse,
    AidocExoticKeywordsResponse,
    AidocExoticOptionsResponse,
    AidocExoticQuestionResponse,
)
```

Methods:

- <code title="post /aidoc-exotic/if-continue-ask">client.aidoc_exotic.<a href="./src/czlai/resources/aidoc_exotic.py">ask_continue</a>(\*\*<a href="src/czlai/types/aidoc_exotic_ask_continue_params.py">params</a>) -> str</code>
- <code title="post /aidoc-exotic/if-need-image">client.aidoc_exotic.<a href="./src/czlai/resources/aidoc_exotic.py">if_need_image</a>(\*\*<a href="src/czlai/types/aidoc_exotic_if_need_image_params.py">params</a>) -> <a href="./src/czlai/types/aidoc_exotic_if_need_image_response.py">object</a></code>
- <code title="post /aidoc-exotic/keywords">client.aidoc_exotic.<a href="./src/czlai/resources/aidoc_exotic.py">keywords</a>(\*\*<a href="src/czlai/types/aidoc_exotic_keywords_params.py">params</a>) -> <a href="./src/czlai/types/aidoc_exotic_keywords_response.py">AidocExoticKeywordsResponse</a></code>
- <code title="post /aidoc-exotic/options">client.aidoc_exotic.<a href="./src/czlai/resources/aidoc_exotic.py">options</a>(\*\*<a href="src/czlai/types/aidoc_exotic_options_params.py">params</a>) -> str</code>
- <code title="post /aidoc-exotic/pic-result">client.aidoc_exotic.<a href="./src/czlai/resources/aidoc_exotic.py">pic_result</a>(\*\*<a href="src/czlai/types/aidoc_exotic_pic_result_params.py">params</a>) -> None</code>
- <code title="post /aidoc-exotic/question">client.aidoc_exotic.<a href="./src/czlai/resources/aidoc_exotic.py">question</a>(\*\*<a href="src/czlai/types/aidoc_exotic_question_params.py">params</a>) -> str</code>
- <code title="post /aidoc-exotic/report">client.aidoc_exotic.<a href="./src/czlai/resources/aidoc_exotic.py">report</a>(\*\*<a href="src/czlai/types/aidoc_exotic_report_params.py">params</a>) -> None</code>
- <code title="post /aidoc-exotic/report-task">client.aidoc_exotic.<a href="./src/czlai/resources/aidoc_exotic.py">report_task</a>(\*\*<a href="src/czlai/types/aidoc_exotic_report_task_params.py">params</a>) -> None</code>
- <code title="post /aidoc-exotic/summary">client.aidoc_exotic.<a href="./src/czlai/resources/aidoc_exotic.py">summarize</a>(\*\*<a href="src/czlai/types/aidoc_exotic_summarize_params.py">params</a>) -> None</code>

# SessionRecords

Methods:

- <code title="post /session-record/history">client.session_records.<a href="./src/czlai/resources/session_records.py">history</a>(\*\*<a href="src/czlai/types/session_record_history_params.py">params</a>) -> None</code>

# MedicalRecords

Types:

```python
from czlai.types import (
    MedicalRecord,
    MedicalRecordRetrieveResponse,
    MedicalRecordCreateListResponse,
)
```

Methods:

- <code title="get /medical-record">client.medical_records.<a href="./src/czlai/resources/medical_records.py">retrieve</a>(\*\*<a href="src/czlai/types/medical_record_retrieve_params.py">params</a>) -> <a href="./src/czlai/types/medical_record_retrieve_response.py">MedicalRecordRetrieveResponse</a></code>
- <code title="put /medical-record">client.medical_records.<a href="./src/czlai/resources/medical_records.py">update</a>(\*\*<a href="src/czlai/types/medical_record_update_params.py">params</a>) -> None</code>
- <code title="post /medical-record-list">client.medical_records.<a href="./src/czlai/resources/medical_records.py">create_list</a>(\*\*<a href="src/czlai/types/medical_record_create_list_params.py">params</a>) -> <a href="./src/czlai/types/medical_record_create_list_response.py">MedicalRecordCreateListResponse</a></code>
- <code title="get /medical-record/ongoing-record">client.medical_records.<a href="./src/czlai/resources/medical_records.py">ongoing_record</a>(\*\*<a href="src/czlai/types/medical_record_ongoing_record_params.py">params</a>) -> None</code>

# AICheckup

Types:

```python
from czlai.types import (
    AICheckupIsFirstResponse,
    AICheckupSessionStartResponse,
    AICheckupSummaryResponse,
    AICheckupUpdateProfileResponse,
)
```

Methods:

- <code title="get /ai-checkup/is-first">client.ai_checkup.<a href="./src/czlai/resources/ai_checkup.py">is_first</a>(\*\*<a href="src/czlai/types/ai_checkup_is_first_params.py">params</a>) -> <a href="./src/czlai/types/ai_checkup_is_first_response.py">AICheckupIsFirstResponse</a></code>
- <code title="post /ai-checkup/pic-result">client.ai_checkup.<a href="./src/czlai/resources/ai_checkup.py">pic_result</a>(\*\*<a href="src/czlai/types/ai_checkup_pic_result_params.py">params</a>) -> None</code>
- <code title="post /ai-checkup/question">client.ai_checkup.<a href="./src/czlai/resources/ai_checkup.py">question</a>(\*\*<a href="src/czlai/types/ai_checkup_question_params.py">params</a>) -> None</code>
- <code title="post /ai-checkup/question-result">client.ai_checkup.<a href="./src/czlai/resources/ai_checkup.py">question_result</a>(\*\*<a href="src/czlai/types/ai_checkup_question_result_params.py">params</a>) -> None</code>
- <code title="post /ai-checkup/report">client.ai_checkup.<a href="./src/czlai/resources/ai_checkup.py">report</a>(\*\*<a href="src/czlai/types/ai_checkup_report_params.py">params</a>) -> None</code>
- <code title="post /ai-checkup/report-task">client.ai_checkup.<a href="./src/czlai/resources/ai_checkup.py">report_task</a>(\*\*<a href="src/czlai/types/ai_checkup_report_task_params.py">params</a>) -> None</code>
- <code title="get /ai-checkup/session-start">client.ai_checkup.<a href="./src/czlai/resources/ai_checkup.py">session_start</a>() -> <a href="./src/czlai/types/ai_checkup_session_start_response.py">AICheckupSessionStartResponse</a></code>
- <code title="post /ai-checkup/summary">client.ai_checkup.<a href="./src/czlai/resources/ai_checkup.py">summary</a>(\*\*<a href="src/czlai/types/ai_checkup_summary_params.py">params</a>) -> str</code>
- <code title="post /ai-checkup/update-profile">client.ai_checkup.<a href="./src/czlai/resources/ai_checkup.py">update_profile</a>(\*\*<a href="src/czlai/types/ai_checkup_update_profile_params.py">params</a>) -> <a href="./src/czlai/types/ai_checkup_update_profile_response.py">AICheckupUpdateProfileResponse</a></code>

# AIConv

Types:

```python
from czlai.types import AIConvAnswerResponse
```

Methods:

- <code title="post /ai-conv/answer">client.ai_conv.<a href="./src/czlai/resources/ai_conv.py">answer</a>(\*\*<a href="src/czlai/types/ai_conv_answer_params.py">params</a>) -> str</code>
- <code title="post /ai-conv/relation">client.ai_conv.<a href="./src/czlai/resources/ai_conv.py">relation</a>(\*\*<a href="src/czlai/types/ai_conv_relation_params.py">params</a>) -> None</code>
- <code title="post /ai-conv/validate">client.ai_conv.<a href="./src/czlai/resources/ai_conv.py">validate</a>(\*\*<a href="src/czlai/types/ai_conv_validate_params.py">params</a>) -> None</code>

# Users

Methods:

- <code title="post /chat-v">client.users.<a href="./src/czlai/resources/users/users.py">chat_v</a>(\*\*<a href="src/czlai/types/user_chat_v_params.py">params</a>) -> None</code>
- <code title="post /logout">client.users.<a href="./src/czlai/resources/users/users.py">logout</a>() -> None</code>
- <code title="post /send-sms">client.users.<a href="./src/czlai/resources/users/users.py">send_sms</a>(\*\*<a href="src/czlai/types/user_send_sms_params.py">params</a>) -> None</code>

## UserInfo

Methods:

- <code title="get /user-info">client.users.user_info.<a href="./src/czlai/resources/users/user_info.py">retrieve</a>(\*\*<a href="src/czlai/types/users/user_info_retrieve_params.py">params</a>) -> None</code>

## Contact

Methods:

- <code title="post /contact">client.users.contact.<a href="./src/czlai/resources/users/contact.py">create</a>(\*\*<a href="src/czlai/types/users/contact_create_params.py">params</a>) -> None</code>

## Summary

Methods:

- <code title="post /summary">client.users.summary.<a href="./src/czlai/resources/users/summary.py">create</a>(\*\*<a href="src/czlai/types/users/summary_create_params.py">params</a>) -> None</code>

## Asr

Methods:

- <code title="post /asr">client.users.asr.<a href="./src/czlai/resources/users/asr.py">create</a>(\*\*<a href="src/czlai/types/users/asr_create_params.py">params</a>) -> None</code>

## Industry

Methods:

- <code title="get /industry">client.users.industry.<a href="./src/czlai/resources/users/industry.py">retrieve</a>() -> None</code>

# Upload

Methods:

- <code title="post /upload">client.upload.<a href="./src/czlai/resources/upload.py">create</a>(\*\*<a href="src/czlai/types/upload_create_params.py">params</a>) -> None</code>

# UploadImage

Methods:

- <code title="post /upload-image">client.upload_image.<a href="./src/czlai/resources/upload_image.py">create</a>(\*\*<a href="src/czlai/types/upload_image_create_params.py">params</a>) -> None</code>

# UploadImageOss

Methods:

- <code title="post /upload-image-oss">client.upload_image_oss.<a href="./src/czlai/resources/upload_image_oss.py">create</a>(\*\*<a href="src/czlai/types/upload_image_oss_create_params.py">params</a>) -> None</code>

# PetProfiles

Types:

```python
from czlai.types import (
    PetProfile,
    PetProfileRetrieveResponse,
    PetProfileListResponse,
    PetProfileDeleteResponse,
    PetProfileVarietyResponse,
)
```

Methods:

- <code title="post /pet-profile">client.pet_profiles.<a href="./src/czlai/resources/pet_profiles.py">create</a>(\*\*<a href="src/czlai/types/pet_profile_create_params.py">params</a>) -> None</code>
- <code title="get /pet-profile">client.pet_profiles.<a href="./src/czlai/resources/pet_profiles.py">retrieve</a>(\*\*<a href="src/czlai/types/pet_profile_retrieve_params.py">params</a>) -> <a href="./src/czlai/types/pet_profile_retrieve_response.py">PetProfileRetrieveResponse</a></code>
- <code title="put /pet-profile">client.pet_profiles.<a href="./src/czlai/resources/pet_profiles.py">update</a>(\*\*<a href="src/czlai/types/pet_profile_update_params.py">params</a>) -> None</code>
- <code title="get /pet-profiles">client.pet_profiles.<a href="./src/czlai/resources/pet_profiles.py">list</a>() -> <a href="./src/czlai/types/pet_profile_list_response.py">PetProfileListResponse</a></code>
- <code title="delete /pet-profile">client.pet_profiles.<a href="./src/czlai/resources/pet_profiles.py">delete</a>(\*\*<a href="src/czlai/types/pet_profile_delete_params.py">params</a>) -> <a href="./src/czlai/types/pet_profile_delete_response.py">PetProfileDeleteResponse</a></code>
- <code title="post /pet-profile/ex-info">client.pet_profiles.<a href="./src/czlai/resources/pet_profiles.py">ex_info</a>(\*\*<a href="src/czlai/types/pet_profile_ex_info_params.py">params</a>) -> None</code>
- <code title="post /pet-profile/variety">client.pet_profiles.<a href="./src/czlai/resources/pet_profiles.py">variety</a>(\*\*<a href="src/czlai/types/pet_profile_variety_params.py">params</a>) -> str</code>

# AIMemes

Types:

```python
from czlai.types import AIMeme, AIMemeCreateResponse, AIMemeRetrieveResponse, AIMemeGenerateResponse
```

Methods:

- <code title="post /ai-meme">client.ai_memes.<a href="./src/czlai/resources/ai_memes.py">create</a>(\*\*<a href="src/czlai/types/ai_meme_create_params.py">params</a>) -> <a href="./src/czlai/types/ai_meme_create_response.py">AIMemeCreateResponse</a></code>
- <code title="get /ai-meme">client.ai_memes.<a href="./src/czlai/resources/ai_memes.py">retrieve</a>(\*\*<a href="src/czlai/types/ai_meme_retrieve_params.py">params</a>) -> <a href="./src/czlai/types/ai_meme_retrieve_response.py">AIMemeRetrieveResponse</a></code>
- <code title="post /ai-meme/generate">client.ai_memes.<a href="./src/czlai/resources/ai_memes.py">generate</a>(\*\*<a href="src/czlai/types/ai_meme_generate_params.py">params</a>) -> <a href="./src/czlai/types/ai_meme_generate_response.py">AIMemeGenerateResponse</a></code>

# MedicationAnalysis

Methods:

- <code title="post /medication_analysis/pic-result">client.medication_analysis.<a href="./src/czlai/resources/medication_analysis.py">pic_result</a>(\*\*<a href="src/czlai/types/medication_analysis_pic_result_params.py">params</a>) -> None</code>
- <code title="post /medication_analysis/report">client.medication_analysis.<a href="./src/czlai/resources/medication_analysis.py">report</a>(\*\*<a href="src/czlai/types/medication_analysis_report_params.py">params</a>) -> None</code>
- <code title="post /medication_analysis/summary">client.medication_analysis.<a href="./src/czlai/resources/medication_analysis.py">summary</a>(\*\*<a href="src/czlai/types/medication_analysis_summary_params.py">params</a>) -> None</code>

# Aipic

Methods:

- <code title="post /aipic/options">client.aipic.<a href="./src/czlai/resources/aipic.py">options</a>(\*\*<a href="src/czlai/types/aipic_options_params.py">params</a>) -> None</code>
- <code title="post /aipic/pic-result">client.aipic.<a href="./src/czlai/resources/aipic.py">pic_result</a>(\*\*<a href="src/czlai/types/aipic_pic_result_params.py">params</a>) -> None</code>
- <code title="post /aipic/question">client.aipic.<a href="./src/czlai/resources/aipic.py">question</a>(\*\*<a href="src/czlai/types/aipic_question_params.py">params</a>) -> None</code>
- <code title="post /aipic/report">client.aipic.<a href="./src/czlai/resources/aipic.py">report</a>(\*\*<a href="src/czlai/types/aipic_report_params.py">params</a>) -> None</code>
- <code title="post /aipic/report-task">client.aipic.<a href="./src/czlai/resources/aipic.py">report_task</a>(\*\*<a href="src/czlai/types/aipic_report_task_params.py">params</a>) -> None</code>
- <code title="post /aipic/validate">client.aipic.<a href="./src/czlai/resources/aipic.py">validate</a>(\*\*<a href="src/czlai/types/aipic_validate_params.py">params</a>) -> None</code>

# Aipics

Methods:

- <code title="post /aipic/summary">client.aipics.<a href="./src/czlai/resources/aipics.py">summary</a>(\*\*<a href="src/czlai/types/aipic_summary_params.py">params</a>) -> None</code>

# AipicExotics

Methods:

- <code title="post /aipic-exotic/options">client.aipic_exotics.<a href="./src/czlai/resources/aipic_exotics.py">options</a>(\*\*<a href="src/czlai/types/aipic_exotic_options_params.py">params</a>) -> None</code>
- <code title="post /aipic-exotic/pic-result">client.aipic_exotics.<a href="./src/czlai/resources/aipic_exotics.py">pic_result</a>(\*\*<a href="src/czlai/types/aipic_exotic_pic_result_params.py">params</a>) -> None</code>
- <code title="post /aipic-exotic/question">client.aipic_exotics.<a href="./src/czlai/resources/aipic_exotics.py">question</a>(\*\*<a href="src/czlai/types/aipic_exotic_question_params.py">params</a>) -> None</code>
- <code title="post /aipic-exotic/report">client.aipic_exotics.<a href="./src/czlai/resources/aipic_exotics.py">report</a>(\*\*<a href="src/czlai/types/aipic_exotic_report_params.py">params</a>) -> None</code>
- <code title="post /aipic-exotic/report-task">client.aipic_exotics.<a href="./src/czlai/resources/aipic_exotics.py">report_task</a>(\*\*<a href="src/czlai/types/aipic_exotic_report_task_params.py">params</a>) -> None</code>
- <code title="post /aipic-exotic/summary">client.aipic_exotics.<a href="./src/czlai/resources/aipic_exotics.py">summary</a>(\*\*<a href="src/czlai/types/aipic_exotic_summary_params.py">params</a>) -> None</code>
- <code title="post /aipic-exotic/validate">client.aipic_exotics.<a href="./src/czlai/resources/aipic_exotics.py">validate</a>(\*\*<a href="src/czlai/types/aipic_exotic_validate_params.py">params</a>) -> None</code>

# AITrials

Methods:

- <code title="post /ai-trial/options">client.ai_trials.<a href="./src/czlai/resources/ai_trials.py">options</a>(\*\*<a href="src/czlai/types/ai_trial_options_params.py">params</a>) -> None</code>
- <code title="post /ai-trial/question">client.ai_trials.<a href="./src/czlai/resources/ai_trials.py">question</a>(\*\*<a href="src/czlai/types/ai_trial_question_params.py">params</a>) -> None</code>

# AITrial

Types:

```python
from czlai.types import AITrialAnswerResponse
```

Methods:

- <code title="post /ai-trial/answer">client.ai_trial.<a href="./src/czlai/resources/ai_trial.py">answer</a>(\*\*<a href="src/czlai/types/ai_trial_answer_params.py">params</a>) -> str</code>
- <code title="post /ai-trial/history">client.ai_trial.<a href="./src/czlai/resources/ai_trial.py">history</a>(\*\*<a href="src/czlai/types/ai_trial_history_params.py">params</a>) -> None</code>
- <code title="post /ai-trial/relation">client.ai_trial.<a href="./src/czlai/resources/ai_trial.py">relation</a>(\*\*<a href="src/czlai/types/ai_trial_relation_params.py">params</a>) -> None</code>
- <code title="post /ai-trial/report">client.ai_trial.<a href="./src/czlai/resources/ai_trial.py">report</a>(\*\*<a href="src/czlai/types/ai_trial_report_params.py">params</a>) -> None</code>
- <code title="post /ai-trial/session-start">client.ai_trial.<a href="./src/czlai/resources/ai_trial.py">session_start</a>(\*\*<a href="src/czlai/types/ai_trial_session_start_params.py">params</a>) -> None</code>
- <code title="post /ai-trial/summary">client.ai_trial.<a href="./src/czlai/resources/ai_trial.py">summary</a>(\*\*<a href="src/czlai/types/ai_trial_summary_params.py">params</a>) -> None</code>

# Policies

Methods:

- <code title="post /policy/policy_info">client.policies.<a href="./src/czlai/resources/policies.py">policy_info</a>(\*\*<a href="src/czlai/types/policy_policy_info_params.py">params</a>) -> None</code>

# MagnumKeys

Methods:

- <code title="post /magnumkey/get-key">client.magnum_keys.<a href="./src/czlai/resources/magnum_keys.py">get_key</a>(\*\*<a href="src/czlai/types/magnum_key_get_key_params.py">params</a>) -> None</code>
- <code title="post /magnumkey/picture-choice">client.magnum_keys.<a href="./src/czlai/resources/magnum_keys.py">picture_choice</a>(\*\*<a href="src/czlai/types/magnum_key_picture_choice_params.py">params</a>) -> None</code>
- <code title="post /magnumkey/picture-question">client.magnum_keys.<a href="./src/czlai/resources/magnum_keys.py">picture_question</a>(\*\*<a href="src/czlai/types/magnum_key_picture_question_params.py">params</a>) -> None</code>
- <code title="post /magnumkey/voice-choice">client.magnum_keys.<a href="./src/czlai/resources/magnum_keys.py">voice_choice</a>(\*\*<a href="src/czlai/types/magnum_key_voice_choice_params.py">params</a>) -> None</code>
- <code title="post /magnumkey/voice-question">client.magnum_keys.<a href="./src/czlai/resources/magnum_keys.py">voice_question</a>(\*\*<a href="src/czlai/types/magnum_key_voice_question_params.py">params</a>) -> None</code>

# Buriedpoints

Methods:

- <code title="post /page-buriedpoint">client.buriedpoints.<a href="./src/czlai/resources/buriedpoints.py">create</a>(\*\*<a href="src/czlai/types/buriedpoint_create_params.py">params</a>) -> None</code>

# Whitelist

Methods:

- <code title="post /whitelist/filtering_data">client.whitelist.<a href="./src/czlai/resources/whitelist.py">filtering_data</a>(\*\*<a href="src/czlai/types/whitelist_filtering_data_params.py">params</a>) -> None</code>
- <code title="post /whitelist/save_data">client.whitelist.<a href="./src/czlai/resources/whitelist.py">save_data</a>(\*\*<a href="src/czlai/types/whitelist_save_data_params.py">params</a>) -> None</code>

# Pets

## PetInfo

Methods:

- <code title="get /pets/pet-info">client.pets.pet_info.<a href="./src/czlai/resources/pets/pet_info.py">retrieve</a>(\*\*<a href="src/czlai/types/pets/pet_info_retrieve_params.py">params</a>) -> None</code>

# UserModuleUsages

Types:

```python
from czlai.types import (
    UserModuleUsageGetAddWecomeBonusResponse,
    UserModuleUsageGetWechatMiniQrcodeResponse,
)
```

Methods:

- <code title="post /user-module-usage/checkin">client.user_module_usages.<a href="./src/czlai/resources/user_module_usages/user_module_usages.py">checkin</a>() -> None</code>
- <code title="post /user-module-usage/get-add-wecome-bonus">client.user_module_usages.<a href="./src/czlai/resources/user_module_usages/user_module_usages.py">get_add_wecome_bonus</a>(\*\*<a href="src/czlai/types/user_module_usage_get_add_wecome_bonus_params.py">params</a>) -> <a href="./src/czlai/types/user_module_usage_get_add_wecome_bonus_response.py">UserModuleUsageGetAddWecomeBonusResponse</a></code>
- <code title="post /user-module-usage/get-wechat-mini-qrcode">client.user_module_usages.<a href="./src/czlai/resources/user_module_usages/user_module_usages.py">get_wechat_mini_qrcode</a>() -> <a href="./src/czlai/types/user_module_usage_get_wechat_mini_qrcode_response.py">UserModuleUsageGetWechatMiniQrcodeResponse</a></code>

## IsAddWecome

Types:

```python
from czlai.types.user_module_usages import IsAddWecomeRetrieveResponse
```

Methods:

- <code title="get /user-module-usage/is-add-wecome">client.user_module_usages.is_add_wecome.<a href="./src/czlai/resources/user_module_usages/is_add_wecome.py">retrieve</a>() -> <a href="./src/czlai/types/user_module_usages/is_add_wecome_retrieve_response.py">IsAddWecomeRetrieveResponse</a></code>

# Logins

Types:

```python
from czlai.types import LoginResponse
```

Methods:

- <code title="post /sms-login">client.logins.<a href="./src/czlai/resources/logins.py">sms</a>(\*\*<a href="src/czlai/types/login_sms_params.py">params</a>) -> <a href="./src/czlai/types/login_response.py">LoginResponse</a></code>
- <code title="post /wechat-login">client.logins.<a href="./src/czlai/resources/logins.py">wechat</a>(\*\*<a href="src/czlai/types/login_wechat_params.py">params</a>) -> None</code>

# UserPoints

Types:

```python
from czlai.types import UserPointRetrieveResponse
```

Methods:

- <code title="get /user-point">client.user_points.<a href="./src/czlai/resources/user_points.py">retrieve</a>() -> <a href="./src/czlai/types/user_point_retrieve_response.py">UserPointRetrieveResponse</a></code>
- <code title="post /user-point/cost-report">client.user_points.<a href="./src/czlai/resources/user_points.py">cost_report</a>(\*\*<a href="src/czlai/types/user_point_cost_report_params.py">params</a>) -> None</code>

# PointPrices

Types:

```python
from czlai.types import PointPriceRetrieveResponse
```

Methods:

- <code title="get /point-price">client.point_prices.<a href="./src/czlai/resources/point_prices.py">retrieve</a>() -> <a href="./src/czlai/types/point_price_retrieve_response.py">PointPriceRetrieveResponse</a></code>

# PointDetails

Types:

```python
from czlai.types import PointDetailRetrieveResponse
```

Methods:

- <code title="get /point-detail">client.point_details.<a href="./src/czlai/resources/point_details.py">retrieve</a>(\*\*<a href="src/czlai/types/point_detail_retrieve_params.py">params</a>) -> <a href="./src/czlai/types/point_detail_retrieve_response.py">PointDetailRetrieveResponse</a></code>

# PointTasks

Types:

```python
from czlai.types import PointTaskListResponse
```

Methods:

- <code title="get /point-task">client.point_tasks.<a href="./src/czlai/resources/point_tasks.py">list</a>() -> <a href="./src/czlai/types/point_task_list_response.py">PointTaskListResponse</a></code>
- <code title="post /point-task/bonus">client.point_tasks.<a href="./src/czlai/resources/point_tasks.py">bonus</a>(\*\*<a href="src/czlai/types/point_task_bonus_params.py">params</a>) -> None</code>
- <code title="post /point-task/confirm">client.point_tasks.<a href="./src/czlai/resources/point_tasks.py">confirm</a>(\*\*<a href="src/czlai/types/point_task_confirm_params.py">params</a>) -> None</code>

# CheckPoints

Methods:

- <code title="post /check-point">client.check_points.<a href="./src/czlai/resources/check_points.py">create</a>(\*\*<a href="src/czlai/types/check_point_create_params.py">params</a>) -> None</code>

# UserAdvices

Methods:

- <code title="post /user-advice">client.user_advices.<a href="./src/czlai/resources/user_advices.py">create</a>(\*\*<a href="src/czlai/types/user_advice_create_params.py">params</a>) -> None</code>

# Evaluation

Methods:

- <code title="post /evaluation/put_evaluation">client.evaluation.<a href="./src/czlai/resources/evaluation.py">put_evaluation</a>(\*\*<a href="src/czlai/types/evaluation_put_evaluation_params.py">params</a>) -> None</code>
