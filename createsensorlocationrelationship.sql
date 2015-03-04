CREATE TABLE things_sensorlocationcrossref (
    id integer NOT NULL,
    date_created timestamp with time zone NOT NULL,
    last_updated timestamp with time zone NOT NULL,
    name character varying(100) NOT NULL,
    description text,
    sensor_id integer NOT NULL,
    location_id integer NOT NULL,
    relationship_type_id integer NOT NULL
);


ALTER TABLE public.things_sensorlocationcrossref OWNER TO ubuntu;

--
-- Name: things_sensorlocationcrossref_id_seq; Type: SEQUENCE; Schema: public; Owner: ubuntu
--

CREATE SEQUENCE things_sensorlocationcrossref_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.things_sensorlocationcrossref_id_seq OWNER TO ubuntu;

--
-- Name: things_sensorlocationcrossref_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ubuntu
--

ALTER SEQUENCE things_sensorlocationcrossref_id_seq OWNED BY things_sensorlocationcrossref.id;


--
-- Name: things_sensorlocationrelationshiptype; Type: TABLE; Schema: public; Owner: ubuntu; Tablespace: 
--

CREATE TABLE things_sensorlocationrelationshiptype (
    id integer NOT NULL,
    date_created timestamp with time zone NOT NULL,
    last_updated timestamp with time zone NOT NULL,
    name character varying(100) NOT NULL,
    description text
);


ALTER TABLE public.things_sensorlocationrelationshiptype OWNER TO ubuntu;

--
-- Name: things_sensorlocationrelationshiptype_id_seq; Type: SEQUENCE; Schema: public; Owner: ubuntu
--

CREATE SEQUENCE things_sensorlocationrelationshiptype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.things_sensorlocationrelationshiptype_id_seq OWNER TO ubuntu;

--
-- Name: things_sensorlocationrelationshiptype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ubuntu
--

ALTER SEQUENCE things_sensorlocationrelationshiptype_id_seq OWNED BY things_sensorlocationrelationshiptype.id;