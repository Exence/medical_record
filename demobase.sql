--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 15.2 (Debian 15.2-1.pgdg100+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: age_insert_trigger_fnc(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.age_insert_trigger_fnc() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
NEW.age = EXTRACT(YEAR FROM age(NEW.examination_date, (SELECT birthday FROM childrens WHERE medcard_num = NEW.medcard_num)))::smallint;
RETURN NEW;
END;
$$;


ALTER FUNCTION public.age_insert_trigger_fnc() OWNER TO postgres;

--
-- Name: childrens_delete_trigger_fnc(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.childrens_delete_trigger_fnc() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
IF OLD.father_id IS NOT NULL THEN
IF (SELECT count(*) FROM childrens WHERE father_id = OLD.father_id) = 0 THEN
DELETE FROM parents WHERE id = OLD.father_id;
END IF;
END IF;
IF OLD.mother_id IS NOT NULL THEN
IF (SELECT count(*) FROM childrens WHERE mother_id = OLD.mother_id) = 0 THEN
DELETE FROM parents WHERE id = OLD.mother_id;
END IF;
END IF;
RETURN OLD;
END;
$$;


ALTER FUNCTION public.childrens_delete_trigger_fnc() OWNER TO postgres;

--
-- Name: on_one_child(integer, integer); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.on_one_child(abs integer, count integer) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
        BEGIN
                RETURN abs::numeric(5,2) / count::numeric(5,2);
        END;
$$;


ALTER FUNCTION public.on_one_child(abs integer, count integer) OWNER TO postgres;

--
-- Name: on_thousand_childrens(integer, integer); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.on_thousand_childrens(abs integer, count integer) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
        BEGIN
                RETURN abs::numeric(5,2) * 1000 / count::numeric(5,2);
        END;
$$;


ALTER FUNCTION public.on_thousand_childrens(abs integer, count integer) OWNER TO postgres;

--
-- Name: percent(integer, integer); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.percent(abs integer, count integer) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
        BEGIN
                RETURN abs::numeric(5,2) / count::numeric(5,2) * 100;
        END;
$$;


ALTER FUNCTION public.percent(abs integer, count integer) OWNER TO postgres;

--
-- Name: users_delete_trigger_fnc(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.users_delete_trigger_fnc() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
IF OLD.access_level = 'db_admin' THEN
IF (SELECT count(*) FROM users WHERE access_level = 'db_admin') = 1 THEN
RAISE EXCEPTION 'Cannot delete last db_admin user';
END IF;
END IF;
RETURN OLD;
END;
$$;


ALTER FUNCTION public.users_delete_trigger_fnc() OWNER TO postgres;

--
-- Name: users_insert_trigger_fnc(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.users_insert_trigger_fnc() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
NEW.login = LOWER(NEW.login);
RETURN NEW;
END;
$$;


ALTER FUNCTION public.users_insert_trigger_fnc() OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: childrens; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.childrens (
    medcard_num integer NOT NULL,
    surname character varying(200) NOT NULL,
    name character varying(200) NOT NULL,
    patronymic character varying(200) NOT NULL,
    kindergarten_num smallint NOT NULL,
    birthday date NOT NULL,
    sex character(1) NOT NULL,
    group_num smallint NOT NULL,
    address character varying(300) NOT NULL,
    clinic character varying(250) NOT NULL,
    edu_type character varying(30) DEFAULT 'ДДУ'::character varying NOT NULL,
    entering_date date NOT NULL,
    father_id integer,
    mother_id integer,
    family_characteristics character(20) NOT NULL,
    family_microclimate character varying(25) NOT NULL,
    rest_and_class_opportunities character varying(30) NOT NULL,
    case_history text,
    CONSTRAINT childrens_family_characteristics_check CHECK (((family_characteristics = 'Полная'::bpchar) OR (family_characteristics = 'Неполная'::bpchar))),
    CONSTRAINT childrens_family_microclimate_check CHECK ((((family_microclimate)::text = 'Благоприятный'::text) OR ((family_microclimate)::text = 'Неблагоприятный'::text))),
    CONSTRAINT childrens_group_num_check CHECK (((group_num >= 1) AND (group_num <= 6))),
    CONSTRAINT childrens_rest_and_class_opportunities_check CHECK ((((rest_and_class_opportunities)::text = 'Комната'::text) OR ((rest_and_class_opportunities)::text = 'Индивидуальный стол'::text) OR ((rest_and_class_opportunities)::text = 'Нет'::text))),
    CONSTRAINT childrens_sex_check CHECK (((sex = 'М'::bpchar) OR (sex = 'Ж'::bpchar)))
);


ALTER TABLE public.childrens OWNER TO postgres;

--
-- Name: kindergartens; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kindergartens (
    number smallint NOT NULL,
    name character varying(200) NOT NULL
);


ALTER TABLE public.kindergartens OWNER TO postgres;

--
-- Name: parents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parents (
    id integer NOT NULL,
    surname character varying(200) NOT NULL,
    name character varying(200) NOT NULL,
    patronymic character varying(200) NOT NULL,
    birthday_year smallint NOT NULL,
    education character(10) NOT NULL,
    phone_num bigint NOT NULL,
    CONSTRAINT parents_education_check CHECK (((education = 'б/обр.'::bpchar) OR (education = 'н/ср.'::bpchar) OR (education = 'ср.'::bpchar) OR (education = 'ср.-спец.'::bpchar) OR (education = 'н/высш.'::bpchar) OR (education = 'высш.'::bpchar))),
    CONSTRAINT parents_phone_num_check CHECK (((phone_num >= '80000000000'::bigint) AND (phone_num <= '89999999999'::bigint)))
);


ALTER TABLE public.parents OWNER TO postgres;

--
-- Name: all_childrens; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.all_childrens AS
 SELECT c.medcard_num,
    c.surname,
    c.name,
    c.patronymic,
    k.name AS kindergarten_name,
    c.birthday,
    c.group_num,
    f.surname AS father_surname,
    f.name AS father_name,
    f.patronymic AS father_patronymic,
    f.phone_num AS father_phone_num,
    m.surname AS mother_surname,
    m.name AS mother_name,
    m.patronymic AS mother_patronymic,
    m.phone_num AS mother_phone
   FROM (((public.childrens c
     LEFT JOIN public.parents f ON ((c.father_id = f.id)))
     LEFT JOIN public.parents m ON ((c.mother_id = m.id)))
     JOIN public.kindergartens k ON ((c.kindergarten_num = k.number)))
  ORDER BY k.name, c.group_num, c.surname, c.name, c.patronymic;


ALTER TABLE public.all_childrens OWNER TO postgres;

--
-- Name: allergyes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.allergyes (
    medcard_num integer NOT NULL,
    allergen character varying(200) NOT NULL,
    allergy_type character varying(35) NOT NULL,
    start_age smallint NOT NULL,
    reaction_type character varying(200) NOT NULL,
    diagnosis_date date NOT NULL,
    note text,
    CONSTRAINT allergyes_allergy_type_check CHECK ((((allergy_type)::text = 'Вакцинальная'::text) OR ((allergy_type)::text = 'Лекарственная'::text) OR ((allergy_type)::text = 'Аллергические заболевания'::text)))
);


ALTER TABLE public.allergyes OWNER TO postgres;

--
-- Name: childrens_medcard_num_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.childrens_medcard_num_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.childrens_medcard_num_seq OWNER TO postgres;

--
-- Name: childrens_medcard_num_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.childrens_medcard_num_seq OWNED BY public.childrens.medcard_num;


--
-- Name: dewormings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dewormings (
    medcard_num integer NOT NULL,
    deworming_date date NOT NULL,
    result text NOT NULL
);


ALTER TABLE public.dewormings OWNER TO postgres;

--
-- Name: dispensaryes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dispensaryes (
    medcard_num integer NOT NULL,
    start_date date NOT NULL,
    diagnosis text NOT NULL,
    specialist character varying(255) NOT NULL,
    end_date date,
    end_reason text
);


ALTER TABLE public.dispensaryes OWNER TO postgres;

--
-- Name: extra_classes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.extra_classes (
    medcard_num integer NOT NULL,
    classes_type character varying(200) NOT NULL,
    age smallint NOT NULL,
    hours_on_week smallint NOT NULL
);


ALTER TABLE public.extra_classes OWNER TO postgres;

--
-- Name: gamma_globulin_injections; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gamma_globulin_injections (
    medcard_num integer NOT NULL,
    vac_date date NOT NULL,
    reason text NOT NULL,
    serial character varying(100) NOT NULL,
    dose numeric(6,3) NOT NULL,
    reaction character varying(22) NOT NULL,
    doctor character varying(250) NOT NULL,
    CONSTRAINT gamma_globulin_injections_reaction_check CHECK (((reaction)::text ~ '^(Не|За)медленная$'::text))
);


ALTER TABLE public.gamma_globulin_injections OWNER TO postgres;

--
-- Name: hospitalizations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hospitalizations (
    medcard_num integer NOT NULL,
    start_date date NOT NULL,
    end_date date,
    diagnosis text NOT NULL,
    founding character varying(255) NOT NULL
);


ALTER TABLE public.hospitalizations OWNER TO postgres;

--
-- Name: mantoux_test; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mantoux_test (
    medcard_num integer NOT NULL,
    check_date date NOT NULL,
    result text NOT NULL
);


ALTER TABLE public.mantoux_test OWNER TO postgres;

--
-- Name: medical_certificates; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.medical_certificates (
    medcard_num integer NOT NULL,
    disease character varying(300) NOT NULL,
    cert_date date NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
    infection_contact boolean NOT NULL,
    sport_exemption_date date,
    vac_exemption_date date,
    doctor character varying(300) NOT NULL
);


ALTER TABLE public.medical_certificates OWNER TO postgres;

--
-- Name: medical_examinations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.medical_examinations (
    medcard_num integer NOT NULL,
    period character varying(80) NOT NULL,
    examination_date date NOT NULL,
    age smallint NOT NULL,
    height numeric(5,2) NOT NULL,
    weight numeric(5,2) NOT NULL,
    complaints text,
    pediatrician text,
    orthopaedist text,
    ophthalmologist text,
    otolaryngologist text,
    dermatologist text,
    neurologist text,
    speech_therapist text,
    denta_surgeon text,
    psychologist text,
    other_doctors text,
    blood_test text,
    urine_analysis text,
    feces_analysis text,
    general_diagnosis text,
    physical_development text,
    mental_development text,
    health_group character varying(3),
    sport_group character varying(16),
    med_and_ped_conclusion text,
    recommendations text,
    doctor character varying(250) NOT NULL,
    CONSTRAINT medical_examinations_health_group_check CHECK (((health_group)::text ~ '^(I{1,3})$|^(IV)$'::text)),
    CONSTRAINT medical_examinations_period_check CHECK ((((period)::text = 'Перед поступлением в ясли-сад, детский сад'::text) OR ((period)::text = 'За 1 год до школы'::text) OR ((period)::text = 'Перед школой'::text))),
    CONSTRAINT medical_examinations_sport_group_check CHECK ((((sport_group)::text = 'Основная'::text) OR ((sport_group)::text = 'Лечебная'::text)))
);


ALTER TABLE public.medical_examinations OWNER TO postgres;

--
-- Name: ongoing_medical_supervisions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ongoing_medical_supervisions (
    medcard_num integer NOT NULL,
    examination_date date NOT NULL,
    examination_data text NOT NULL,
    diagnosis text NOT NULL,
    prescription text,
    doctor character varying(250) NOT NULL
);


ALTER TABLE public.ongoing_medical_supervisions OWNER TO postgres;

--
-- Name: oral_sanations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oral_sanations (
    medcard_num integer NOT NULL,
    sanation_date date NOT NULL,
    dental_result text NOT NULL,
    sanation_result text NOT NULL
);


ALTER TABLE public.oral_sanations OWNER TO postgres;

--
-- Name: parents_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.parents_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parents_id_seq OWNER TO postgres;

--
-- Name: parents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.parents_id_seq OWNED BY public.parents.id;


--
-- Name: past_illnesses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.past_illnesses (
    medcard_num integer NOT NULL,
    start_date date NOT NULL,
    end_date date,
    diagnosis text NOT NULL
);


ALTER TABLE public.past_illnesses OWNER TO postgres;

--
-- Name: prevaccination_checkups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prevaccination_checkups (
    medcard_num integer NOT NULL,
    examination_date date NOT NULL,
    age smallint NOT NULL,
    diagnosis text NOT NULL,
    report text NOT NULL,
    vac_name_id smallint NOT NULL,
    no_vac_date date,
    doctor character varying(255) NOT NULL
);


ALTER TABLE public.prevaccination_checkups OWNER TO postgres;

--
-- Name: screenings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.screenings (
    medcard_num integer NOT NULL,
    examination_date date NOT NULL,
    age smallint NOT NULL,
    questionnaire_test character varying(20) NOT NULL,
    height numeric(5,2) NOT NULL,
    weight numeric(5,2) NOT NULL,
    physical_development character varying(30),
    blood_pressures character varying(30),
    carriage character varying(50),
    foot_condition character varying(20),
    sight_od numeric(3,2),
    sight_os numeric(3,2),
    visual_acuity character varying(20),
    malinovsky_test character varying(20),
    binocular_vision character varying(20),
    hearing_acuteness character varying(20),
    dynammetry_left numeric(3,1),
    dynammetry_right numeric(3,1),
    physical_fitness character varying(20),
    protein_in_urine character varying(25),
    glucose_in_urine character varying(30),
    biological_age character varying(30),
    speech_defects boolean,
    kern_test boolean,
    neurotic_disorders boolean,
    thinking_and_speech boolean,
    motor_development boolean,
    attention_and_memory boolean,
    social_contacts boolean,
    diseases_for_year smallint,
    CONSTRAINT screenings_binocular_vision_check CHECK ((((binocular_vision)::text = 'Норма'::text) OR ((binocular_vision)::text = 'Нарушение'::text))),
    CONSTRAINT screenings_biological_age_check CHECK ((((biological_age)::text = 'Соответствует'::text) OR ((biological_age)::text = 'Опережает'::text) OR ((biological_age)::text = 'Отстает'::text))),
    CONSTRAINT screenings_carriage_check CHECK ((((carriage)::text = 'Нормальная'::text) OR ((carriage)::text = 'Незначительные отклонения'::text) OR ((carriage)::text = 'Значительные нарушения'::text))),
    CONSTRAINT screenings_foot_condition_check CHECK ((((foot_condition)::text = 'Нормальная'::text) OR ((foot_condition)::text = 'Уплощена'::text) OR ((foot_condition)::text = 'Плоская'::text))),
    CONSTRAINT screenings_glucose_in_urine_check CHECK ((((glucose_in_urine)::text = 'Норма'::text) OR ((glucose_in_urine)::text = 'Глюкоза в моче'::text))),
    CONSTRAINT screenings_hearing_acuteness_check CHECK ((((hearing_acuteness)::text = 'Норма'::text) OR ((hearing_acuteness)::text = 'Снижена'::text))),
    CONSTRAINT screenings_malinovsky_test_check CHECK ((((malinovsky_test)::text = 'Нормальная'::text) OR ((malinovsky_test)::text = 'Предмиопия'::text))),
    CONSTRAINT screenings_physical_development_check CHECK ((((physical_development)::text = 'Нормальное'::text) OR ((physical_development)::text = 'Низкий рост'::text) OR ((physical_development)::text = 'Дефицит массы'::text) OR ((physical_development)::text = 'Избыток массы'::text))),
    CONSTRAINT screenings_physical_fitness_check CHECK ((((physical_fitness)::text = 'Норма'::text) OR ((physical_fitness)::text = 'Снижена'::text) OR ((physical_fitness)::text = 'Повышена'::text))),
    CONSTRAINT screenings_protein_in_urine_check CHECK ((((protein_in_urine)::text = 'Норма'::text) OR ((protein_in_urine)::text = 'Следы белка'::text) OR ((protein_in_urine)::text = 'Белок в моче'::text))),
    CONSTRAINT screenings_questionnaire_test_check CHECK ((((questionnaire_test)::text = 'Норма'::text) OR ((questionnaire_test)::text = 'Отклонение'::text))),
    CONSTRAINT screenings_visual_acuity_check CHECK ((((visual_acuity)::text = 'Нормальная'::text) OR ((visual_acuity)::text = 'Снижена'::text)))
);


ALTER TABLE public.screenings OWNER TO postgres;

--
-- Name: spa_treatments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spa_treatments (
    medcard_num integer NOT NULL,
    start_date date NOT NULL,
    end_date date,
    diagnosis text NOT NULL,
    founding_specialization character varying(255) NOT NULL,
    climatic_zone character varying(255) NOT NULL
);


ALTER TABLE public.spa_treatments OWNER TO postgres;

--
-- Name: tuberculosis_vaccinations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tuberculosis_vaccinations (
    medcard_num integer NOT NULL,
    vac_date date NOT NULL,
    serial character varying(100) NOT NULL,
    dose numeric(6,3) NOT NULL,
    doctor character varying(250) NOT NULL
);


ALTER TABLE public.tuberculosis_vaccinations OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    login character varying(40) NOT NULL,
    surname character varying(200) NOT NULL,
    name character varying(200) NOT NULL,
    patronymic character varying(200) NOT NULL,
    password_hash character varying(255) NOT NULL,
    access_level character varying(15) NOT NULL,
    kindergarten_num smallint,
    CONSTRAINT users_access_level_check CHECK ((((access_level)::text = 'db_admin'::text) OR ((access_level)::text = 'admin'::text) OR ((access_level)::text = 'user'::text)))
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: vac_names; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vac_names (
    id integer NOT NULL,
    name character varying(200) NOT NULL
);


ALTER TABLE public.vac_names OWNER TO postgres;

--
-- Name: vac_names_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vac_names_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vac_names_id_seq OWNER TO postgres;

--
-- Name: vac_names_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vac_names_id_seq OWNED BY public.vac_names.id;


--
-- Name: vaccinations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vaccinations (
    medcard_num integer NOT NULL,
    vac_name_id smallint NOT NULL,
    vac_type character varying(30) NOT NULL,
    vac_date date NOT NULL,
    serial character varying(100) NOT NULL,
    dose numeric(6,3) NOT NULL,
    introduction_method character varying(100) NOT NULL,
    reaction character varying(22) NOT NULL,
    doctor character varying(250) NOT NULL,
    CONSTRAINT vaccinations_reaction_check CHECK (((reaction)::text ~ '^(Не|За)медленная$'::text)),
    CONSTRAINT vaccinations_vac_type_check CHECK ((((vac_type)::text ~ '^Вакцинация ?I{1,3}$'::text) OR ((vac_type)::text ~ '^Ревакцинация ?I{1,3}?V{0,1}$'::text)))
);


ALTER TABLE public.vaccinations OWNER TO postgres;

--
-- Name: visit_specialist_controls; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.visit_specialist_controls (
    medcard_num integer NOT NULL,
    start_dispanser_date date NOT NULL,
    assigned_date date NOT NULL,
    fact_date date
);


ALTER TABLE public.visit_specialist_controls OWNER TO postgres;

--
-- Name: childrens medcard_num; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.childrens ALTER COLUMN medcard_num SET DEFAULT nextval('public.childrens_medcard_num_seq'::regclass);


--
-- Name: parents id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parents ALTER COLUMN id SET DEFAULT nextval('public.parents_id_seq'::regclass);


--
-- Name: vac_names id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vac_names ALTER COLUMN id SET DEFAULT nextval('public.vac_names_id_seq'::regclass);


--
-- Data for Name: allergyes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.allergyes (medcard_num, allergen, allergy_type, start_age, reaction_type, diagnosis_date, note) FROM stdin;
3	Пыльца трав	Вакцинальная	2	Аллергическая реакция I типа	2023-04-09	
44	Трезвость	Аллергические заболевания	2	Смерть	2021-06-16	Такие дела
\.


--
-- Data for Name: childrens; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.childrens (medcard_num, surname, name, patronymic, kindergarten_num, birthday, sex, group_num, address, clinic, edu_type, entering_date, father_id, mother_id, family_characteristics, family_microclimate, rest_and_class_opportunities, case_history) FROM stdin;
3	Иванов	Артем	Игоревич	1	2019-04-03	М	1	Полярные Зори, 4, кв. 37	Городская детская поликлиника №1	ДДУ	2022-09-12	18	19	Полная              	Благоприятный	Комната	До десятого колена все здоровы как быки
4	Кудряшов	Иннокентий	Арсеньевич	1	2019-09-23	М	1	Мирная ул., д. 9 кв.199	Городская детская поликлиника №1	ДДУ	2022-07-27	20	21	Полная              	Благоприятный	Комната	
5	Халипова	Таисия	Максимовна	1	2018-07-11	Ж	2	Чкалова ул., д. 6 кв.148	Городская детская поликлиника №1	ДДУ	2020-07-23	22	23	Полная              	Благоприятный	Комната	
39	Ермишина	Юлия	Егоровна	1	2019-05-04	Ж	2	Новый пер., д. 4 кв.167	Городская детская поликлиника №2	ДДУ	2021-07-27	57	\N	Неполная            	Благоприятный	Комната	
40	Ханцева	Марьяна	Павловна	1	2019-05-24	Ж	2	Комсомольская ул., д. 20 кв.166	Городская детская поликлиника №4	ДДУ	2021-07-23	58	59	Полная              	Неблагоприятный	Нет	
6	Бакшаев	Никита	Никанорович	1	2019-06-05	М	2	Чкалова ул., д. 6 кв.148	Городская детская поликлиника №3	ДДУ	2021-07-27	\N	24	Неполная            	Благоприятный	Индивидуальный стол	
44	Балаев	Виктор	Юрьевич	1	2019-11-11	М	4	Радищева, д. 26	Городская детская поликлиника №1	ДДУ	2022-09-12	96	\N	Неполная            	Неблагоприятный	Нет	Отец алконавт
\.


--
-- Data for Name: dewormings; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dewormings (medcard_num, deworming_date, result) FROM stdin;
3	2023-03-01	Отрицательно
\.


--
-- Data for Name: dispensaryes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dispensaryes (medcard_num, start_date, diagnosis, specialist, end_date, end_reason) FROM stdin;
3	2022-01-01	Гастроэнтерит	Гастроэнтеролог	2023-01-06	Выздоровление
\.


--
-- Data for Name: extra_classes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.extra_classes (medcard_num, classes_type, age, hours_on_week) FROM stdin;
44	Пьянка	2	5
3	Музыка	3	5
\.


--
-- Data for Name: gamma_globulin_injections; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gamma_globulin_injections (medcard_num, vac_date, reason, serial, dose, reaction, doctor) FROM stdin;
\.


--
-- Data for Name: hospitalizations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.hospitalizations (medcard_num, start_date, end_date, diagnosis, founding) FROM stdin;
3	2022-03-01	2022-03-31	Перелом лучевой кости со смещением. Произведена отрытая репозиция.	Городской травмотологический центр
\.


--
-- Data for Name: kindergartens; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.kindergartens (number, name) FROM stdin;
0	admins
1	МБДОУ Детский сад №1
2	МБДОУ Детский сад №2
3	МБДОУ Детский сад №3
4	МБДОУ Детский сад №4
\.


--
-- Data for Name: mantoux_test; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mantoux_test (medcard_num, check_date, result) FROM stdin;
\.


--
-- Data for Name: medical_certificates; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.medical_certificates (medcard_num, disease, cert_date, start_date, end_date, infection_contact, sport_exemption_date, vac_exemption_date, doctor) FROM stdin;
3	ОРВИ	2023-01-13	2023-01-01	2023-01-12	f	2023-04-13	\N	Иванов Иван Иванович
\.


--
-- Data for Name: medical_examinations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.medical_examinations (medcard_num, period, examination_date, age, height, weight, complaints, pediatrician, orthopaedist, ophthalmologist, otolaryngologist, dermatologist, neurologist, speech_therapist, denta_surgeon, psychologist, other_doctors, blood_test, urine_analysis, feces_analysis, general_diagnosis, physical_development, mental_development, health_group, sport_group, med_and_ped_conclusion, recommendations, doctor) FROM stdin;
\.


--
-- Data for Name: ongoing_medical_supervisions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ongoing_medical_supervisions (medcard_num, examination_date, examination_data, diagnosis, prescription, doctor) FROM stdin;
\.


--
-- Data for Name: oral_sanations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.oral_sanations (medcard_num, sanation_date, dental_result, sanation_result) FROM stdin;
3	2023-03-01	28 гнилых зубов	Вылечены все
\.


--
-- Data for Name: parents; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.parents (id, surname, name, patronymic, birthday_year, education, phone_num) FROM stdin;
96	Балаев	Юрий	Владимирович	1989	ср.       	89062885288
20	Кудряшов	Арсений	Степанович	1981	н/высш.   	89254875454
21	Кудряшова	Виктория	Егоровна	1984	ср.-спец. 	89619715818
22	Халипов	Максим	Адамович	1976	высш.     	89578445214
23	Халипова	Евгения	Юрьевна	1976	высш.     	89525484565
24	Бакшаева	Дарья	Даниловна	1989	ср.-спец. 	89526583785
57	Ермишин	Егор	Сергеевич	1977	ср.-спец. 	89526587456
58	Ханцев	Павел	Валентинович	1980	ср.       	89734092573
59	Ханцева	Диана	Леонидовна	1984	б/обр.    	89283691556
18	Иванов	Игорь	Владимирович	1979	ср.-спец. 	89587415789
19	Иванова	Светлана	Сергеевна	1984	высш.     	89857845125
\.


--
-- Data for Name: past_illnesses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.past_illnesses (medcard_num, start_date, end_date, diagnosis) FROM stdin;
3	2022-01-01	2022-01-21	Ветряная оспа
\.


--
-- Data for Name: prevaccination_checkups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.prevaccination_checkups (medcard_num, examination_date, age, diagnosis, report, vac_name_id, no_vac_date, doctor) FROM stdin;
\.


--
-- Data for Name: screenings; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.screenings (medcard_num, examination_date, age, questionnaire_test, height, weight, physical_development, blood_pressures, carriage, foot_condition, sight_od, sight_os, visual_acuity, malinovsky_test, binocular_vision, hearing_acuteness, dynammetry_left, dynammetry_right, physical_fitness, protein_in_urine, glucose_in_urine, biological_age, speech_defects, kern_test, neurotic_disorders, thinking_and_speech, motor_development, attention_and_memory, social_contacts, diseases_for_year) FROM stdin;
\.


--
-- Data for Name: spa_treatments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.spa_treatments (medcard_num, start_date, end_date, diagnosis, founding_specialization, climatic_zone) FROM stdin;
3	2023-04-01	2023-04-13	Хронические заболевания сердечно-сосудистой системы	Болезни системы кровообращения	Тропическая (Юг)
\.


--
-- Data for Name: tuberculosis_vaccinations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tuberculosis_vaccinations (medcard_num, vac_date, serial, dose, doctor) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (login, surname, name, patronymic, password_hash, access_level, kindergarten_num) FROM stdin;
ivanovaii	Иванова	Ирина	Ивановна	$2b$12$JLlgjWeZJgl4vwRgFod6TeS2wVx5RoCjzXvZU667Vf6Ldhn3BZye6	admin	0
petrovaln	Петрова	Лидия	Николаевна	$2b$12$76WnkuBTULwvA7UbR722VuMv69LWbRIZ/pTy7Exxd7PMuaAZ37swC	user	1
novikovaea	Новикова	Елена	Александровна	$2b12$yGKYmzfbGPgth1Njw13Qs.bDNdiZ1USqFmkeXq2e/k0GVIPggtD2G	user	2
mansurovan	Мансуров	Алишер	Набижонович	$2b$12$KzPoAm0vigvGjXDyJa8zauydpwzNlpd4BAjoqfFjfvc3FK0ImECFC	db_admin	0
\.


--
-- Data for Name: vac_names; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vac_names (id, name) FROM stdin;
1	Полиомиелит
2	Дифтерия
3	Коклюш
4	Столбняк
5	Паротит
6	Корь
7	Гепатит «В»
8	Краснуха
\.


--
-- Data for Name: vaccinations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vaccinations (medcard_num, vac_name_id, vac_type, vac_date, serial, dose, introduction_method, reaction, doctor) FROM stdin;
\.


--
-- Data for Name: visit_specialist_controls; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.visit_specialist_controls (medcard_num, start_dispanser_date, assigned_date, fact_date) FROM stdin;
3	2022-01-01	2023-04-10	2023-04-10
3	2022-01-01	2023-04-13	2023-04-13
3	2022-01-01	2023-04-11	2023-04-11
\.


--
-- Name: childrens_medcard_num_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.childrens_medcard_num_seq', 44, true);


--
-- Name: parents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.parents_id_seq', 96, true);


--
-- Name: vac_names_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vac_names_id_seq', 8, true);


--
-- Name: allergyes allergyes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.allergyes
    ADD CONSTRAINT allergyes_pkey PRIMARY KEY (medcard_num, allergen);


--
-- Name: childrens childrens_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.childrens
    ADD CONSTRAINT childrens_pkey PRIMARY KEY (medcard_num);


--
-- Name: dewormings dewormings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dewormings
    ADD CONSTRAINT dewormings_pkey PRIMARY KEY (medcard_num, deworming_date);


--
-- Name: dispensaryes dispensaryes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispensaryes
    ADD CONSTRAINT dispensaryes_pkey PRIMARY KEY (medcard_num, start_date);


--
-- Name: extra_classes extra_classes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.extra_classes
    ADD CONSTRAINT extra_classes_pkey PRIMARY KEY (medcard_num, classes_type, age);


--
-- Name: gamma_globulin_injections gamma_globulin_injections_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gamma_globulin_injections
    ADD CONSTRAINT gamma_globulin_injections_pkey PRIMARY KEY (medcard_num, vac_date);


--
-- Name: hospitalizations hospitalizations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hospitalizations
    ADD CONSTRAINT hospitalizations_pkey PRIMARY KEY (medcard_num, start_date);


--
-- Name: kindergartens kindergartens_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kindergartens
    ADD CONSTRAINT kindergartens_name_key UNIQUE (name);


--
-- Name: kindergartens kindergartens_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kindergartens
    ADD CONSTRAINT kindergartens_pkey PRIMARY KEY (number);


--
-- Name: mantoux_test mantoux_test_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mantoux_test
    ADD CONSTRAINT mantoux_test_pkey PRIMARY KEY (medcard_num, check_date);


--
-- Name: medical_certificates medical_certificates_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medical_certificates
    ADD CONSTRAINT medical_certificates_pkey PRIMARY KEY (medcard_num, disease, cert_date);


--
-- Name: medical_examinations medical_examinations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medical_examinations
    ADD CONSTRAINT medical_examinations_pkey PRIMARY KEY (medcard_num, period);


--
-- Name: ongoing_medical_supervisions ongoing_medical_supervisions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ongoing_medical_supervisions
    ADD CONSTRAINT ongoing_medical_supervisions_pkey PRIMARY KEY (medcard_num, examination_date);


--
-- Name: oral_sanations oral_sanations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oral_sanations
    ADD CONSTRAINT oral_sanations_pkey PRIMARY KEY (medcard_num, sanation_date);


--
-- Name: parents parents_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parents
    ADD CONSTRAINT parents_pkey PRIMARY KEY (id);


--
-- Name: past_illnesses past_illnesses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.past_illnesses
    ADD CONSTRAINT past_illnesses_pkey PRIMARY KEY (medcard_num, diagnosis, start_date);


--
-- Name: prevaccination_checkups prevaccination_checkups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prevaccination_checkups
    ADD CONSTRAINT prevaccination_checkups_pkey PRIMARY KEY (medcard_num, examination_date);


--
-- Name: screenings screenings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.screenings
    ADD CONSTRAINT screenings_pkey PRIMARY KEY (medcard_num, examination_date);


--
-- Name: spa_treatments spa_treatments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spa_treatments
    ADD CONSTRAINT spa_treatments_pkey PRIMARY KEY (medcard_num, start_date);


--
-- Name: tuberculosis_vaccinations tuberculosis_vaccinations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tuberculosis_vaccinations
    ADD CONSTRAINT tuberculosis_vaccinations_pkey PRIMARY KEY (medcard_num, vac_date);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (login);


--
-- Name: vac_names vac_names_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vac_names
    ADD CONSTRAINT vac_names_pkey PRIMARY KEY (id);


--
-- Name: vaccinations vaccinations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vaccinations
    ADD CONSTRAINT vaccinations_pkey PRIMARY KEY (medcard_num, vac_name_id, vac_type);


--
-- Name: visit_specialist_controls visit_specialist_controls_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.visit_specialist_controls
    ADD CONSTRAINT visit_specialist_controls_pkey PRIMARY KEY (medcard_num, start_dispanser_date, assigned_date);


--
-- Name: childrens childrens_delete_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER childrens_delete_trigger AFTER DELETE ON public.childrens FOR EACH ROW EXECUTE FUNCTION public.childrens_delete_trigger_fnc();


--
-- Name: medical_examinations medical_examinations_insert_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER medical_examinations_insert_trigger BEFORE INSERT ON public.medical_examinations FOR EACH ROW EXECUTE FUNCTION public.age_insert_trigger_fnc();


--
-- Name: prevaccination_checkups prevaccination_checkups_insert_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER prevaccination_checkups_insert_trigger BEFORE INSERT ON public.prevaccination_checkups FOR EACH ROW EXECUTE FUNCTION public.age_insert_trigger_fnc();


--
-- Name: screenings screenings_insert_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER screenings_insert_trigger BEFORE INSERT ON public.screenings FOR EACH ROW EXECUTE FUNCTION public.age_insert_trigger_fnc();


--
-- Name: users users_delete_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER users_delete_trigger BEFORE DELETE ON public.users FOR EACH ROW EXECUTE FUNCTION public.users_delete_trigger_fnc();


--
-- Name: users users_insert_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER users_insert_trigger BEFORE INSERT ON public.users FOR EACH ROW EXECUTE FUNCTION public.users_insert_trigger_fnc();


--
-- Name: allergyes allergyes_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.allergyes
    ADD CONSTRAINT allergyes_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: childrens childrens_father_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.childrens
    ADD CONSTRAINT childrens_father_id_fkey FOREIGN KEY (father_id) REFERENCES public.parents(id) ON DELETE SET NULL;


--
-- Name: childrens childrens_kindergarten_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.childrens
    ADD CONSTRAINT childrens_kindergarten_num_fkey FOREIGN KEY (kindergarten_num) REFERENCES public.kindergartens(number) ON DELETE RESTRICT;


--
-- Name: childrens childrens_mother_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.childrens
    ADD CONSTRAINT childrens_mother_id_fkey FOREIGN KEY (mother_id) REFERENCES public.parents(id) ON DELETE SET NULL;


--
-- Name: dewormings dewormings_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dewormings
    ADD CONSTRAINT dewormings_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: dispensaryes dispensaryes_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispensaryes
    ADD CONSTRAINT dispensaryes_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: extra_classes extra_classes_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.extra_classes
    ADD CONSTRAINT extra_classes_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: gamma_globulin_injections gamma_globulin_injections_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gamma_globulin_injections
    ADD CONSTRAINT gamma_globulin_injections_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: hospitalizations hospitalizations_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hospitalizations
    ADD CONSTRAINT hospitalizations_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: mantoux_test mantoux_test_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mantoux_test
    ADD CONSTRAINT mantoux_test_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: medical_certificates medical_certificates_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medical_certificates
    ADD CONSTRAINT medical_certificates_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: medical_examinations medical_examinations_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medical_examinations
    ADD CONSTRAINT medical_examinations_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: ongoing_medical_supervisions ongoing_medical_supervisions_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ongoing_medical_supervisions
    ADD CONSTRAINT ongoing_medical_supervisions_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: oral_sanations oral_sanations_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oral_sanations
    ADD CONSTRAINT oral_sanations_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: past_illnesses past_illnesses_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.past_illnesses
    ADD CONSTRAINT past_illnesses_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: prevaccination_checkups prevaccination_checkups_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prevaccination_checkups
    ADD CONSTRAINT prevaccination_checkups_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: prevaccination_checkups prevaccination_checkups_vac_name_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prevaccination_checkups
    ADD CONSTRAINT prevaccination_checkups_vac_name_id_fkey FOREIGN KEY (vac_name_id) REFERENCES public.vac_names(id) ON DELETE RESTRICT;


--
-- Name: screenings screenings_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.screenings
    ADD CONSTRAINT screenings_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: spa_treatments spa_treatments_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spa_treatments
    ADD CONSTRAINT spa_treatments_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: tuberculosis_vaccinations tuberculosis_vaccinations_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tuberculosis_vaccinations
    ADD CONSTRAINT tuberculosis_vaccinations_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: users users_kindergarten_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_kindergarten_num_fkey FOREIGN KEY (kindergarten_num) REFERENCES public.kindergartens(number) ON DELETE RESTRICT;


--
-- Name: vaccinations vaccinations_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vaccinations
    ADD CONSTRAINT vaccinations_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: vaccinations vaccinations_vac_name_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vaccinations
    ADD CONSTRAINT vaccinations_vac_name_id_fkey FOREIGN KEY (vac_name_id) REFERENCES public.vac_names(id) ON DELETE RESTRICT;


--
-- Name: visit_specialist_controls visit_specialist_controls_medcard_num_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.visit_specialist_controls
    ADD CONSTRAINT visit_specialist_controls_medcard_num_fkey FOREIGN KEY (medcard_num) REFERENCES public.childrens(medcard_num) ON DELETE CASCADE;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--