--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employee (id, email, last_name, first_name, patronymic, post) FROM stdin;
a19419f3-6c48-4f5e-84fb-a362fa683976	korochun@yandex.ru	Балашов	Дмитрий	Викторович	Ведущий инженер-исследователь
0e93f99b-98a8-4a3b-8360-fdd466b44347	smirnov@mail.ru	Смирнов	Олег	\N	\N
ba35b4ae-f945-4b7e-ab40-d3273b66714c	petrov@mail.ru	Петров	Петр	\N	\N
a68bbe83-ef46-4fa0-ab48-4a45112d7401	test@prom.com	Тестов	Тест	Тестович	техник
\.


--
-- Data for Name: task; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.task (id, name, content, period_of_execution, parent_id, status, employee_id) FROM stdin;
57dbe370-8426-4381-a8b7-20942be58cc7	Доработка интерфейса	Требуется изменить интерфейс по замечаниям потребителей	2024-04-28 07:57:40.708483+03	\N	1	a19419f3-6c48-4f5e-84fb-a362fa683976
bc679b84-378d-4929-98ef-a0fe78850270	Кнопка Выход	Поменять местами кнопку выход с Принять	2024-04-28 19:35:00+03	57dbe370-8426-4381-a8b7-20942be58cc7	1	a19419f3-6c48-4f5e-84fb-a362fa683976
db0517fe-f95c-40e0-bdf2-b5e3ce7a24d9	task1	Тестируем 1	\N	\N	0	\N
969e3cf6-a780-4d99-a82b-0e2aebbbad7a	task 2	Тестируем 2	\N	\N	1	ba35b4ae-f945-4b7e-ab40-d3273b66714c
5b486e2c-3652-46fc-add5-402b0956701d	task 3	Тестируем 3	\N	\N	0	\N
6dd46529-81b5-4a9c-b27b-416233b8dcd5	task 11	Тестируем 4	\N	db0517fe-f95c-40e0-bdf2-b5e3ce7a24d9	0	\N
\.
