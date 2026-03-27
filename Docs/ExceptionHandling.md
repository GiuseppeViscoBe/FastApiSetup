                ┌──────────────────────┐
                │       CLIENT         │
                │  (Swagger / HTTP)   │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │       ROUTER         │
                │  (FastAPI endpoint)  │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │       SERVICE        │
                │  Business Logic      │
                │                      │
                │  if error:           │
                │  raise Exception ────┐
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │        CRUD          │
                │   DB operations      │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │       DATABASE       │
                └──────────────────────┘


❗ EXCEPTION PATH
────────────────────────────────────────────────────────────

            Exception raised in Service / CRUD
                          │
                          ▼
                ┌──────────────────────┐
                │   FASTAPI ENGINE     │
                │ (Exception catcher)  │
                └─────────┬────────────┘
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
        ▼                                   ▼
┌──────────────────────┐        ┌────────────────────────┐
│ BaseAppException ?   │        │ Other Exception ?      │
│ (your custom errors) │        │ (bugs, DB errors, etc) │
└─────────┬────────────┘        └──────────┬─────────────┘
          │ YES                             │ YES
          ▼                                 ▼
┌────────────────────────────┐   ┌────────────────────────────┐
│ base_app_exception_handler │   │ generic_exception_handler  │
│                            │   │                            │
│ uses:                      │   │ uses:                      │
│ - exc.message              │   │ - logs traceback           │
│ - exc.status_code          │   │ - returns 500              │
└─────────┬──────────────────┘   └──────────┬─────────────────┘
          │                                 │
          ▼                                 ▼
     JSONResponse                     JSONResponse
 (custom status + message)        (500 Internal Error)
          │                                 │
          └──────────────┬──────────────────┘
                         ▼
                ┌──────────────────────┐
                │       CLIENT         │
                │  (receives JSON)     │
                └──────────────────────┘