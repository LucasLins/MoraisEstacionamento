-- Database: MoraisEstacionamento2

-- DROP DATABASE "MoraisEstacionamento2";

CREATE DATABASE "MoraisEstacionamento2"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Table: public.contas

-- DROP TABLE public.contas;

CREATE TABLE IF NOT EXISTS public.contas
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 0 MINVALUE 0 MAXVALUE 1000 CACHE 1 ),
    usuario text COLLATE pg_catalog."default" NOT NULL,
    senha text COLLATE pg_catalog."default" NOT NULL,
    tipo character(1) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT contas_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.contas
    OWNER to postgres;

-- Table: public.estacionamentos

-- DROP TABLE public.estacionamentos;

CREATE TABLE IF NOT EXISTS public.estacionamentos
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 0 MINVALUE 0 MAXVALUE 1000 CACHE 1 ),
    nome text COLLATE pg_catalog."default" NOT NULL,
    totalcarro integer NOT NULL,
    totalmoto integer NOT NULL,
    totalcaminhao integer NOT NULL,
    valor double precision NOT NULL,
    vagascarro integer NOT NULL,
    vagasmoto integer NOT NULL,
    vagascaminhao integer NOT NULL,
    avisomsg text COLLATE pg_catalog."default" NOT NULL DEFAULT 'Nenhum aviso no momento'::text,
    avisotitulo text COLLATE pg_catalog."default" DEFAULT 'Aviso'::text,
    CONSTRAINT estacionamentos_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.estacionamentos
    OWNER to postgres;

-- Table: public.funcionarios

-- DROP TABLE public.funcionarios;

CREATE TABLE IF NOT EXISTS public.funcionarios
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 0 MINVALUE 0 MAXVALUE 1000 CACHE 1 ),
    idconta integer NOT NULL,
    idestacionamento integer NOT NULL,
    nome text COLLATE pg_catalog."default" NOT NULL,
    sexo character(1) COLLATE pg_catalog."default" NOT NULL,
    cpf text COLLATE pg_catalog."default" NOT NULL,
    telefone text COLLATE pg_catalog."default" NOT NULL,
    email text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT funcionarios_pkey PRIMARY KEY (id),
    CONSTRAINT conta_fkey FOREIGN KEY (idconta)
        REFERENCES public.contas (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT estacionamento_fkey FOREIGN KEY (idestacionamento)
        REFERENCES public.estacionamentos (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.funcionarios
    OWNER to postgres;

-- Table: public.gestores

-- DROP TABLE public.gestores;

CREATE TABLE IF NOT EXISTS public.gestores
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 0 MINVALUE 0 MAXVALUE 1000 CACHE 1 ),
    idconta integer NOT NULL,
    nome text COLLATE pg_catalog."default" NOT NULL,
    sexo character(1) COLLATE pg_catalog."default" NOT NULL,
    cpf text COLLATE pg_catalog."default" NOT NULL,
    telefone text COLLATE pg_catalog."default" NOT NULL,
    email text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT gestor_pkey PRIMARY KEY (id),
    CONSTRAINT conta_fkey FOREIGN KEY (id)
        REFERENCES public.contas (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.gestores
    OWNER to postgres;

-- Table: public.registros

-- DROP TABLE public.registros;

CREATE TABLE IF NOT EXISTS public.registros
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 0 MINVALUE 0 MAXVALUE 10000 CACHE 1 ),
    idfuncionario integer NOT NULL,
    placa text COLLATE pg_catalog."default" NOT NULL,
    tipo text COLLATE pg_catalog."default" NOT NULL,
    valorpagar double precision,
    pago boolean,
    idestacionamento integer NOT NULL,
    dataentrada timestamp without time zone NOT NULL,
    datasaida timestamp without time zone,
    CONSTRAINT registros_pkey PRIMARY KEY (id),
    CONSTRAINT funcionario_fkey FOREIGN KEY (idfuncionario)
        REFERENCES public.funcionarios (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.registros
    OWNER to postgres;