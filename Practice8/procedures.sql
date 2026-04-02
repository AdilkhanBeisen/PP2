CREATE OR REPLACE PROCEDURE upsert_contact(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(p text)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts WHERE name=p OR phone=p;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_m(names text[], phones text[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    invalid_phones TEXT[] := '{}';
BEGIN
   for i in 1.. array_length(names,1) LOOP

    IF phones[i]~ '^\d+$' THEN
        INSERT INTO contacts(name, phone) VALUES(names[i], phones[i]);

    ELSE
        invalid_phones := array_append(invalid_phones, phones[i]);
    END IF;

    END LOOP;
    RAISE NOTICE 'Invalid phones: %', invalid_phones;
END;
$$;

