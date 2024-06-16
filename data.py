"""Data for work."""

expected_columns_old = [
        'Vendor \nПоставщик',
        'Purchase Order\nНомер Заказа',
        "Contractor's Document Number \nНомер документа Поставщика (Подрядчика)",
        "Contractor's Revision\nРевизия Подрядчика",
        "Owner's Document number \nНомер документа Заказчика",
        'English Document Title \nНазвание документа на английском языке',
        'Russian Document Title \nНазвание документа на русском языке',
        'Doc. Type (VDR code)\nТип док-та',
        'Sequence',
        "Owner's Revision\n Ревизия\nЗаказчика",
        'Rev. Date\n Дата рев.',
        'Reason for issue\nПричина выпуска',
        'Confidential Class\nКонфиденциальный класс',
        'Language\nЯзык док-та',
        ' No of Sheets\nКол-во листов',
        ' Liquidated damages\n(YES/NO)',
        'PLIP Code\nКод PLIP',
        'TAG No.\nТаговый номер',
        'Discipline\nДисциплина',
        'Construction area\nНомер стр.зоны',
        'Plant Unit\nУстановка',
        'Building number\nНомер здания',
        'System \n(sub-system)\nСистема (подсистема)',
        'Vendor-SEI review TRM No\nNo TRM от Поставщика к SEI',
        'Actual TRM Date\nФактическая дата ТRМ',
        'Planned TRM Date (1st Submission)\nПлан. дата TRM (1-я представление)',
        'Forecast TRM Date\nПрогноз Дата ТRМ',
        'Current Version\nТекущая версия',
        'Key Documents\n（For DXS reference）',
        "Contractor's Review Code\nКод рассмотрения Подрядчика",
        'Contractor-Owner review TRM No\nNo TRM от Подрядчика к Заказчику',
        'Planned Review TRM Date (1st Submission)\n'
        'План. дата Review TRM (1-я представление)',
        'Actual Review TRM Date (Current Submission)\nФакт. дата Review TRM ',
        "Owner's \nReview Code\nКод рассмотрения Заказчика",
        "Owner's CRS TRM No\nNo CRS TRM Заказчика",
        "Owner's CRS TRM Date\nДата CRS \nTRM Заказчика",
        'TM Remarks (Distribution Type)\nТребования к предоставлению\nна рассмотрение',
        'Native File Required\nТребование к исходному формату файла',
        'Hard-Copy (Original) Required\nТребование ооригиналу ',
        "Part of Final Vendor's Documentation\n"
        'В ходит в объём итоговой док-ции Поставщика',
        'Contractor-Owner Soft-Copy TRM No\n'
        '(-.pdf & native file, if applicable)\n'
        'No TRM от Подрядчика к Заказчику \n'
        'на эл.версию\n'
        '(-.pdf и формат разработки, если применимо)',
        'Actual SC \nTRM Date\nФакт. дата TRM на эл. версию',
        'Contractor-Owner hard-copy TRM No\n'
        'No TRM от Подрядчика к Заказчику \n'
        'на бум.версию',
        'Actual HC \nTRM Date\nФакт. дата TRM на бум. версию',
        'Planned HC \nTRM Date\nПлан. дата TRM \nна бум. версию',
        'Remarks \nПримечания',
]


expected_columns = ['Action\nСтатус документа',
                    'Order document code\nШифр заказного документа',
                    'Activity ID\nИдентификатор вида работ',
                    'Vendor \nПоставщик',
                    'Purchase Order\nНомер Заказа',
                    "Owner's Document number \nНомер документа Заказчика",
                    "Vendor's Document number \nНомер документа Поставщика (если применимо)",
                    'English Document Title \nНазвание документа на английском языке',
                    'Russian Document Title \nНазвание документа на русском языке',
                    'Doc. Type (VDR code)\nТип док-та',
                    "Owner's Revision\n Ревизия\nЗаказчика",
                    'Rev. Date\n Дата рев.',
                    'Reason for issue\nПричина выпуска',
                    'Confidential Class\nКонфиденциальный класс',
                    'Language\nЯзык док-та',
                    ' No of Sheets\nКол-во листов',
                    'TAG No.\nТаговый номер',
                    'Discipline\nДисциплина',
                    'Construction area\nНомер стр.зоны',
                    'Building number\nНомер здания',
                    'System \n(sub-system)\nСистема (подсистема)',
                    'Vendor-Owner review TRM No\nNo TRM от Поставщика к Заказчику',
                    'Planned Review TRM Date (1st Submission)\n'
                    'План. дата Review TRM (1-я представление)',
                    'Actual Review TRM Date (Current Submission)\nФакт. дата Review TRM ',
                    "Owner's \nReview Code\nКод рассмотрения Заказчика",
                    "Owner's CRS TRM No\nNo CRS TRM Заказчика",
                    "Owner's CRS TRM Date\nДата CRS \nTRM Заказчика",
                    'TM Remarks (Distribution Type)\nТребования к предоставлению\nна рассмотрение',
                    'Native File Required\nТребование к исходному формату файла',
                    'Hard-Copy (Original) Required\nТребование ооригиналу ',
                    "Part of Final Vendor's Documentation\n"
                    'В ходит в объём финальной док-ции Поставщика',
                    'Contractor-Owner Soft-Copy TRM No\n'
                    '(-.pdf & native file, if applicable)\n'
                    'No TRM от Поставщика к Заказчику \n'
                    'на эл.версию\n'
                    '(-.pdf и формат разработки, если применимо)',
                    'Actual SC \nTRM Date\nФакт. дата TRM на эл. версию',
                    'Vendor-Owner hard-copy TRM No\n'
                    'No TRM от Поставщика к Заказчику \n'
                    'на бум.версию',
                    'Actual HC \nTRM Date\nФакт. дата TRM на бум. версию',
                    'Planned HC \nTRM Date\nПлан. дата TRM \nна бум. версию',
                    'Remarks Примечания',
                    ]

material_req_name = 'MATERIAL REQUISITION N. / \nЗАКАЗНАЯ СПЕЦИФИКАЦИЯ'
equipment_name = 'EQUIPMENT TITLE /НАЗВАНИЕ ОБОРУДОВАНИЯ:'
