PGDMP     9    6                y            academiafitBD    14.1    14.1     t           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            u           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            v           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            w           1262    24979    academiafitBD    DATABASE     o   CREATE DATABASE "academiafitBD" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "academiafitBD";
                postgres    false            ?            1259    24980    academiafitApp_appsetting    TABLE     z   CREATE TABLE public."academiafitApp_appsetting" (
    id bigint NOT NULL,
    logo_img character varying(100) NOT NULL
);
 /   DROP TABLE public."academiafitApp_appsetting";
       public         heap    postgres    false            ?            1259    24983     academiafitApp_appsetting_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."academiafitApp_appsetting_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public."academiafitApp_appsetting_id_seq";
       public          postgres    false    209            x           0    0     academiafitApp_appsetting_id_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE public."academiafitApp_appsetting_id_seq" OWNED BY public."academiafitApp_appsetting".id;
          public          postgres    false    210            ?           2604    25160    academiafitApp_appsetting id    DEFAULT     ?   ALTER TABLE ONLY public."academiafitApp_appsetting" ALTER COLUMN id SET DEFAULT nextval('public."academiafitApp_appsetting_id_seq"'::regclass);
 M   ALTER TABLE public."academiafitApp_appsetting" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    209            p          0    24980    academiafitApp_appsetting 
   TABLE DATA           C   COPY public."academiafitApp_appsetting" (id, logo_img) FROM stdin;
    public          postgres    false    209   ?       y           0    0     academiafitApp_appsetting_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public."academiafitApp_appsetting_id_seq"', 6, true);
          public          postgres    false    210            ?           2606    25196 8   academiafitApp_appsetting academiafitApp_appsetting_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public."academiafitApp_appsetting"
    ADD CONSTRAINT "academiafitApp_appsetting_pkey" PRIMARY KEY (id);
 f   ALTER TABLE ONLY public."academiafitApp_appsetting" DROP CONSTRAINT "academiafitApp_appsetting_pkey";
       public            postgres    false    209            p      x?3?L,(???O?/??zy?\1z\\\ xb	     