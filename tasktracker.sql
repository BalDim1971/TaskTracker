
--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employee (id, email, last_name, first_name, patronymic, post) FROM stdin;
a19419f3-6c48-4f5e-84fb-a362fa683976	korochun@yandex.ru	Балашов	Дмитрий	Викторович	Ведущий инженер-исследователь
0e93f99b-98a8-4a3b-8360-fdd466b44347	smirnov@mail.ru	Смирнов	Олег	\N	\N
ba35b4ae-f945-4b7e-ab40-d3273b66714c	petrov@mail.ru	Петров	Петр	\N	\N
\.


--
-- Data for Name: task; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.task (id, name, content, period_of_execution, parent_id, status, employee_id) FROM stdin;
57dbe370-8426-4381-a8b7-20942be58cc7	Доработка интерфейса	Требуется изменить интерфейс по замечаниям потребителей	2024-04-28 07:57:40.708483+03	\N	1	a19419f3-6c48-4f5e-84fb-a362fa683976
bc679b84-378d-4929-98ef-a0fe78850270	Кнопка Выход	Поменять местами кнопку выход с Принять	2024-04-28 19:35:00+03	57dbe370-8426-4381-a8b7-20942be58cc7	1	a19419f3-6c48-4f5e-84fb-a362fa683976
db0517fe-f95c-40e0-bdf2-b5e3ce7a24d9	task1	Тестируем 1	\N	\N	0	\N
969e3cf6-a780-4d99-a82b-0e2aebbbad7a	task 2	Тестируем 2	\N	\N	0	\N
\.
