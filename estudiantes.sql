PGDMP      !                }           universidad_db    16.0    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16443    universidad_db    DATABASE     �   CREATE DATABASE universidad_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_World.1252';
    DROP DATABASE universidad_db;
                postgres    false            �            1259    16445    estudiantes    TABLE     �   CREATE TABLE public.estudiantes (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    carrera character varying(50) NOT NULL,
    "año_ingreso" integer NOT NULL,
    promedio numeric(3,2) NOT NULL
);
    DROP TABLE public.estudiantes;
       public         heap    postgres    false            �            1259    16444    estudiantes_id_seq    SEQUENCE     �   CREATE SEQUENCE public.estudiantes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.estudiantes_id_seq;
       public          postgres    false    216            �           0    0    estudiantes_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.estudiantes_id_seq OWNED BY public.estudiantes.id;
          public          postgres    false    215                       2604    16448    estudiantes id    DEFAULT     p   ALTER TABLE ONLY public.estudiantes ALTER COLUMN id SET DEFAULT nextval('public.estudiantes_id_seq'::regclass);
 =   ALTER TABLE public.estudiantes ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            �          0    16445    estudiantes 
   TABLE DATA           T   COPY public.estudiantes (id, nombre, carrera, "año_ingreso", promedio) FROM stdin;
    public          postgres    false    216   N       �           0    0    estudiantes_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.estudiantes_id_seq', 3, true);
          public          postgres    false    215                       2606    16450    estudiantes estudiantes_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.estudiantes
    ADD CONSTRAINT estudiantes_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.estudiantes DROP CONSTRAINT estudiantes_pkey;
       public            postgres    false    216            �   {   x�3��M,:�6Q!��ʢ�*Nϼ�Լ�T��g^Z~Q��%�ɉ�FF�&z�\F�ΉE9��
>�7 ����d&g恕�ps:�%*� �I/�qI-JM��*1�*15������ z(}     