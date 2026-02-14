# Proyecto para la Auto generación de códigos para Items de Inventarios
## **arkCodeGenerator** 

Este proyecto va dirigido a solucionar de manera rápida y fácil la generación de código para los ítems de inventarios partiendo de una lógica funcional operativa basado en criterios de orden y agrupamiento y para lo cual se deben tener en consideración algunos parámetros pre establecidos, para ello debemos definir los siguientes principios:

#### I. El usuario debe establecer las siguientes reglas:
    A. Tamaño mínimo y máximo del código.
    B. Definir su estructura y tipos de caracteres que lo componen.
    C. Dentro de la estructura se debe definir el significado de cada grupo de dígitos
    D. Establecer los diferentes niveles que componen la estructura de código, Ejemplo:
        1. Nivel 1 = Familia o Departamento (Dos Dígitos) (A)
        2. Nivel 2 = Categoría (Tres Dígitos) (B)
        3. Nivel 3 = Sub Categoría (Dos Dígitos) (C)
        4. Nivel 4 = Clases (Tres Dígitos) (D)
        5. Nivel 5 = Correlativo del Producto o Servicio (Cuatro Dígitos) (X)
               AABBBCCDDXXXX
    E. Determinar el tipo de separado si lo lleva entre niveles, solo se deben permitir guion (-) o guion bajo (_)  y  alertar que si el cliente utiliza impresoras fiscales para el proceso de facturación no deben incluir ningún tipo de carácter especial (ª, º, !, “·$%/)=¿?=))
    F. El Tamaño del código estará definido por la concatenación de los Niveles descritos en el apartado “D”
### II. La interfaz gráfica será desarrollada utilizando Python con pyside6, y debe mantener el estilo estándar ya utilizado en la aplicación ARKToolsPC, aun cuando pueden establecerse modificaciones en los estilos.
### III. La base de datos sera SQLite, en el inicio debe estar estructurada de la siguiente manera

####   *A. -- Tabla: ark_company*
        1. emp_IDauto INTEGER PRIMARY KEY AUTOINCREMENT, 
        2. emp_code TEXT CONSTRAINT Requerido NOT NULL ON CONFLICT ROLLBACK, 
        3. emp_description TEXT, 
        4. emp_tax_id TEXT, 
        5. emp_Status INTEGER DEFAULT 1, 
        6. emp_tax_address TEXT, 
        7. emp_local_address TEXT, emp_Telefono1 TEXT, 
        8. emp_mobile TEXT, 
        9. emp_legal_representative TEXT, 
        10. emp_legal_representative_id  TEXT,
        11. emp_phone TEXT, 
        12. emp_contact_email TEXT, 
        13. emp_company_email TEXT, 
        14. emp_tipo_taxpayer INTEGER, 
        15. emp_create_date TEXT DEFAULT (datetime('now')), 
        16. emp_systemdate TEXT, 
        17. emp_systemtime TEXT, 
        18. emp_namemachine TEXT, 
        19. emp_usercreator TEXT, 
        20. emp_lastupdatedate TEXT, 
        21. emp_lastupdatetime TEXT, 
        22. emp_lastmachine TEXT, 
        23. emp_userlastupdate TEXT;

####    *B. -- Tabla: ark_clients*
            1. clt_IDauto INTEGER PRIMARY KEY AUTOINCREMENT, 
            2. clt_code TEXT NOT NULL, 
            3. clt_description TEXT, 
            4. clt_tax_id TEXT, 
            5. clt_Status INTEGER DEFAULT 1, 
            6. clt_tax_address TEXT, 
            7. clt_local_address TEXT, 
            8. clt_phone TEXT, 
            9. clt_mobile TEXT, 
            10. clt_legal_representative TEXT, 
            11. clt_legal_representative_id TEXT, 
            12. clt_contact_phone TEXT, 
            13. clt_contact_email TEXT, 
            14. clt_client_email TEXT, 
            15. clt_tipo_taxpayer INTEGER, 
            16. clt_Origen TEXT, 
            17. clt_codeOrigen TEXT, 
            18. clt_create_date TEXT DEFAULT (datetime('now')), 
            19. clt_systemdate TEXT, 
            20. clt_systemtime TEXT, 
            21. clt_namemachine TEXT, 
            22. clt_usercreator TEXT, 
            23. clt_lastupdatedate TEXT, 
            24. clt_lastupdatetime TEXT, 
            25. clt_lastmachine TEXT, 
            26. clt_userlastupdate TEXT;
   
####    *C. --Tabla: ark_levels*
            27. lvs_IDauto INTEGER PRIMARY KEY AUTOINCREMENT, 
            28. lvs_code TEXT NOT NULL, 
            29. lvs_description TEXT, 
            30. lvs_descriptionTec TEXT,
            31. lvs_level_type TEXT,
            32. lvs_Number_of_digits TEXT,
            33. lvs_Special_characters TEXT,
            34. lvs_Level_separator TEXT,
            35. lvs_Alphanumeric TEXT,
            36. lvs_Status INTEGER DEFAULT 1, 
            37. lvs_create_date TEXT DEFAULT (datetime('now')), 
            38. lvs_systemdate TEXT, 
            39. lvs_systemtime TEXT,
            40. lvs_namemachine TEXT,
            41. lvs_usercreator TEXT,
            42. lvs_lastupdatedate TEXT,
            43. lvs_lastupdatetime TEXT,
            44. lvs_lastmachine TEXT,
            45. lvs_userlastupdate TEXT;
               
####    *D. --Tabla: ark_auto_code_generator*
            46. acg_Idauto INTEGER PRIMARY KEY AUTOINCREMENT,
            47. acg_codeid TEXT NOT NULL, 
            48. acg_first_level TEXT,
            49. acg_second_level TEXT,
            50. acg_third_level TEXT,
            51. acg_fourth_level TEXT,
            52. acg_fifth_level TEXT, 
            53. acg_auto_code TEXT,
            54. acg_create_date TEXT DEFAULT (datetime('now')), 
            55. acg_systemdate TEXT, 
            56. acg_systemtime TEXT,
            57. acg_namemachine TEXT,
            58. acg_usercreator TEXT,
            59. acg_lastupdatedate TEXT,
            60. acg_lastupdatetime TEXT,
            61. acg_lastmachine TEXT,
            62. acg_userlastupdate TEXT;
