nssm install <servicename> <program> [<arguments>]
-----------------------------
nssm remove _save2csv
<!--
nssm install "_save2csv" ^
"C:/dev/__bite_dev/sc_meta/dump_ex2csv/save2csv_deploy/dist/save2csv_deploy.exe" ^
"C:/dev/__bite_dev/sc_meta/dump_ex2csv/files/Отчёт/Istoria_Posescheniy(1).xlsx", ^ C:/dev/__bite_dev/sc_meta/dump_ex2csv/files/Отчёт/save2csv ^-->

nssm install _save2csv C:\dev\__bite_dev\sc_meta\dump_ex2csv\save2csv_deploy\dist\save2csv_deploy.exe

<!-- 
nssm set _save2csv Application C:\dev\__bite_dev\sc_meta\dump_ex2csv\save2csv_deploy\dist\save2csv_deploy.exe
-->
nssm set _save2csv AppParameters C:\dev\__bite_dev\sc_meta\dump_ex2csv\files\Отчёт\Istoria_Posescheniy(1).xlsx C:\dev\__bite_dev\sc_meta\dump_ex2csv\files\Отчёт\save2csv

nssm set _save2csv AppRestartDelay 120000	<!-- Рестарт каждые 2 минуты *60*1000 -->

nssm set _save2csv AppStdout C:\dev\__bite_dev\sc_meta\dump_ex2csv\save2csv_deploy 
<!-- Stdout -> в лог -->

-----------------------------
*NAME:*
_save2csv

# PROD
*PATH:*

*STARTUP DIRECTORY:*

*ARGS:*
"C:/dev/__bite_dev/sc_meta/dump_ex2csv/files/Отчёт/Istoria_Posescheniy (1).xlsx", C:/dev/__bite_dev/sc_meta/dump_ex2csv/files/Отчёт/save2csv

*CMD:*
"C:/dev/__bite_dev/sc_meta/dump_ex2csv/files/Отчёт/Istoria_Posescheniy(1).xlsx" "C:/dev/__bite_dev/sc_meta/dump_ex2csv/files/Отчёт/save2csv"

# TEST
*PATH:*
C:/Users/artemiy.ogloblin/AppData/Local/Programs/Python/Python39/python.exe

*STARTUP DIRECTORY:*
C:/dev/__bite_dev/sc_meta/dump_ex2csv

*ARGS:*
C:/dev/__bite_dev/sc_meta/dump_ex2csv/files/source.xlsx, C:/dev/__bite_dev/sc_meta/dump_ex2csv/files/

*cmd:*
"C:/dev/__bite_dev/sc_meta/dump_ex2csv/files/source.xlsx" "C:/dev/__bite_dev/sc_meta/dump_ex2csv/files"


