--start datatype conversion tests
SELECT COUNT(*) AS total_rows
--
, sum(case when cast(src.VALID_FROM_TEXT as datatype) = tgt.VALID_FROM_DATE then 1 else 0 end) as VALID_FROM_DATE_pass_count
, sum(case when cast(src.VALID_FROM_TEXT as datatype) = tgt.VALID_FROM_DATE then 0 else 1 end) as VALID_FROM_DATE_fail_count
--
, sum(case when cast(src.PAYMENT_TEXT as datatype) = tgt.PAYMENT_DATE then 1 else 0 end) as PAYMENT_DATE_pass_count
, sum(case when cast(src.PAYMENT_TEXT as datatype) = tgt.PAYMENT_DATE then 0 else 1 end) as PAYMENT_DATE_fail_count
--
, sum(case when cast(src.END_TEXT as datatype) = tgt.END_DATE then 1 else 0 end) as END_DATE_pass_count
, sum(case when cast(src.END_TEXT as datatype) = tgt.END_DATE then 0 else 1 end) as END_DATE_fail_count
--
, sum(case when cast(src.START_TEXT as datatype) = tgt.START_DATE then 1 else 0 end) as START_DATE_pass_count
, sum(case when cast(src.START_TEXT as datatype) = tgt.START_DATE then 0 else 1 end) as START_DATE_fail_count
--
FROM TARGET_SCHEMA.TARGET_TABLE tgt 
--
--
JOIN TARGET_SCHEMA.TARGET_TABLE tgt ON src.load_id = tgt.load_id
--replace pseudocode w/real joins
AND tgt.keys = src.keys
--
WHERE tgt.LOAD_ID = :LOAD_ID;
--stop datatype conversion tests
--
--
