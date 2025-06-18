# Fullstack Web Development with Python <!-- omit in toc -->

### [# goit-pythonweb-hw-02](https://github.com/topics/goit-pythonweb-hw-02) <!-- omit in toc -->

<p align="center">
  <img align="center" src="./assets/thumbnail.svg" width="200" title="Project thumbnail" alt="project thumbnail">
</p>


## Basics of Docker Technology <!-- omit in toc -->

This project demonstrates the containerization of a [FastAPI](https://fastapi.tiangolo.com/) application using [Docker](https://www.docker.com/). The task involved integrating a [PostgreSQL](https://hub.docker.com/_/postgres) database into a shared [Docker Compose](https://docs.docker.com/compose/) setup, enabling all services to run together seamlessly. The solution includes automation for building and running containers for convenient development and to ensure consistent environment setup.

In addition to the FastAPI application and PostgreSQL database, the setup includes optional pgAdmin with preset database server as a database management tool — all running within a unified Docker Compose environment.

> ⚠️This configuration is optimized for local development only!
> For collaborative development or production use, further refinements are recommended to enhance security, scalability, and operational reliability.

## Table of Contents <!-- omit in toc -->
- [Task Requirements](#task-requirements)
  - [Technical Description](#technical-description)
  - [Acceptance Criteria](#acceptance-criteria)
- [Task Solution](#task-solution)
    - [Project files](#project-files)
    - [Docker Hub](#docker-hub)
    - [UML Deployment Diagram](#uml-deployment-diagram)
    - [Solution Screenshots](#solution-screenshots)
      - [Application successful setup screenshots](#application-successful-setup-screenshots)
  - [What have been done](#what-have-been-done)
    - [Additional Solution Comments](#additional-solution-comments)
    - [Optimisations](#optimisations)
    - [Fixes](#fixes)
    - [Potential future improvements](#potential-future-improvements)
- [Project Setup \& Run Instructions](#project-setup--run-instructions)
  - [Prerequisites](#prerequisites)
  - [Setting Up the Development Environment](#setting-up-the-development-environment)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Choose Setup Method](#2-choose-setup-method)
      - [🐳 Option 1: Using Docker (_Recommended_)](#-option-1-using-docker-recommended)
      - [🐍 Option 2: Local Virtual Environment](#-option-2-local-virtual-environment)

## Task Requirements

This task focuses on the practical deployment of a FastAPI application using Docker.

You need to clone a FastAPI-based project, configure it, and run it in a Docker container. After setting up the environment, you must verify that the application runs correctly and connects successfully to the PostgreSQL database.

### Technical Description

1. Clone the repository [github.com/GoIT-Python-Web/FullStack-Web-Development-hw2](https://github.com/GoIT-Python-Web/FullStack-Web-Development-hw2) using `git clone` and step into:
    ```bash
    git clone https://github.com/GoIT-Python-Web/FullStack-Web-Development-hw2
    cd FullStack-Web-Development-hw2
    ```
2. Create a `Dockerfile` with instructions to build the Docker image for the application.
    > ⚠️ Note: Use Python 3.10 to ensure compatibility.
3. Write a `docker-compose.yaml` file with configurations for both the FastAPI app and the PostgreSQL database.
4. Use Docker Compose to:
    * Build the environment
    * Start the containers using:
        ```bash
        docker-compose up
        ```

    > 💡 Tip:
    > Update the `SQLALCHEMY_DATABASE_URL` in `\conf\db.py` to use the name of your PostgreSQL service (from `docker-compose.yaml`) instead of `localhost`.
    > 
    > Example update:
    > ```python
    > SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:567234@localhost:5432/hw02"
    > ```
    > When using Docker Compose, containers run in a shared virtual network.
    >  This means services should communicate using their service name as the hostname instead of localhost.
5. Verify application functionality and database connection.
    After launching the container, you should see a welcome page in the browser.
    ![welcome page](./assets/task-requirements/tr1.png)
    If everything is set-up properly in `docker-compose.yaml`, clicking the "**Check DB**" button should confirm that the application is connected to the database.
    ![confirmation that the application is connected to the database](./assets/task-requirements/tr1.png)
    > ❗ If you see a red error message instead of "Welcome to FastAPI!", it likely means the database connection was not configured correctly.

### Acceptance Criteria

* Repository has been cloned, and a valid `Dockerfile` has been created.
* A working `docker-compose.yaml` is written for both the app and the PostgreSQL service.
* The environment is successfully built and launched using `docker-compose up`.
* The FastAPI app is functional and successfully connected to the database (as verified by the "**Check DB**" button).

## Task Solution

This project demonstrates containerization of FastAPI with PostgreSQL using Docker Compose, optimized for local development.

#### Project files

Solution for this task is located in the following files:
* [requirements.txt](./requirements.txt) - file with all project dependencies.
* [Dockerfile](./Dockerfile) - file with instructions to build the Docker image for the application.
* [.dockerignore](./.dockerignore) - file with ignored files and directories during image build.
* [Docker compose file](./compose.yaml) - file with configurations for both the FastAPI app and the PostgreSQL database, incl. optional pgAdmin tooling.
* [.env.example](./.env.example) - example for user file (`.env`) with application settings.
* [init/](./init/) - folder with initialization scripts for:
    * PostgreSQL database - has its own [Readme description](./init/db/Readme.md) with motivation to have it.
    * pgAdmin - has its own [Readme description](./init/pgadmin/Readme.md)  with motivation to have it.
* [src/](./src/) - folder with FastAPI (backend + frontend) application.
* [.python-version](./.python-version) - optional settings for [pyenv](https://github.com/pyenv/pyenv) to set version of Python (tested with pyenv version 2.6.1).

#### Docker Hub

This project is also published to [Docker Hub](https://hub.docker.com/r/rmsh/goit-pythonweb-hw-02).

You can pull and run it directly:

```bash
docker pull rmsh/goit-pythonweb-hw-02
```

Then run it:
```bash
docker run -p 8000:8000 rmsh/goit-pythonweb-hw-02
```

> 📝 Note:
> You still need a PostgreSQL database to connect to. Either use the provided docker-compose.yml, or connect to your own database.

#### UML Deployment Diagram

![UML Deployment Diagram](./assets/uml/DeploymentDiagram.jpg)

#### Solution Screenshots

##### Application successful setup screenshots

Successful application run and connection to the database:

![task solution screenshot](./assets/results/task_successful_setup_screenshot.png)

List of containers in Docker Desktop application:

![task solution screenshot](./assets/results/task_containers_list_screenshot.png)

Containers status, together with health status:

![task solution screenshot](./assets/results/task_containers_status_screenshot.png)


### What have been done

#### Additional Solution Comments

* For easier setup of project settings and better security `.env` file containing environmental variables approach was used to contain all main project settings like user and database names, user passwords, exposed ports, etc. To create `.env` file, [.env.example](./.env.example) was provided - use it content as a start point.
    `.env` file should not be under version control or disclosed in any way.
* Added health check for the containers in [compose.yaml](./compose.yaml) to check their state.
    Now there is possibility to see if there is something wrong with a specific running container:
    ![healthcheck feature](./assets/results/features/healthcheck.png)
* Added [pgAdmin](https://www.pgadmin.org/download/pgadmin-4-container/) (used [official image](https://hub.docker.com/r/dpage/pgadmin4/) for this) as an additional embedded into environment tool for the environment to be more self-contained and easily managed. Requires no other external tools to be used outwards environment to access and manage database and it is automatically set-up (by [init scripts](./init/pgadmin/)) to access exact instance of database.
May be included by invoking using `tools` profile when starting compose environment:
    ```bash
    docker compose --profile tools up -d
    ```
    > Note: The optional `-d` flag here means run application in so-called "detached mode". It runs your containers in the background — like a daemon.

    pgAdmin login page (by default accessible at [localhost:5050](http://localhost:5050/)) require separate pgAdmin credentials:
    ![pgadmin login page](./assets/results/features/pgadmin1.png)

    Prompt to enter database password:
    ![pgadmin enter database password](./assets/results/features/pgadmin2.png)

    Fully-featured automatically generated database access:
    ![pgadmin database access](./assets/results/features/pgadmin3.png)

#### Optimisations

* Moved FastApi application related files into the separate [src/](./src/) folder to separate it from other project files.
    While building Docker image all contained in the `src/` folder files are copied into respective `/app` working directory inside container.
    This enhancement allows to maintain clean project structure and reduces necessity to update [.dockerignore][.dockerignore] file so often.
* Minimalistic Python alpine base images required some additional dependencies to be added and build (not required by full Python image). This increased overall image build time and its size. To optimize this dependency:
    ```requirements.txt
    psycopg2==2.9.9 ; python_version >= "3.10" and python_version < "4.0"
    ```
    was replaced with already built binary dependency:
    ```requirements.txt
    psycopg2-binary==2.9.9 ; python_version >= "3.10" and python_version < "4.0"
    ```
    This allowed to avoid installing `gcc`, `musl-dev`, `python3-dev`, and `postgresql-dev`, that alone can save several hundred MB.
* Removed (commented out) unused dependencies from installation in [requirements.txt](./requirements.txt) to reduce final image size:
    ```requirements.txt
    faker==20.1.0 ; python_version >= "3.10" and python_version < "4.0"   # Move to dev if only for testing
    pymongo==4.6.1 ; python_version >= "3.10" and python_version < "4.0"  # Avoid if MongoDB isn't core
    ```
* Added [.dockerignore](./.dockerignore) file that exclude some files that are not required in final `web` service container (e.g. documentation, cache, virtual environment, etc.) and will ignored while building `web` service image.
    Now web container contains only necessary app files:
    ![app files after dockerignore](./assets/results/features/dockerignore.png)
* Optimize Docker image build in [Dockerfile](./Dockerfile) by:
    * Space optimization:
        Usage of alpine image for Python version3:10 to reduce final image size.
        > Note:
        Some standard full-size image features may be absent and may require workarounds or additional installation.
    * Space optimization: 
        Prevent Python from writing `.pyc` files to disk (Python recompiles on-the-fly anyway).
        ```Dockerfile
        ENV PYTHONDONTWRITEBYTECODE=1
        ```
        This prevents `.pyc` & `__pycache__` from being generated (saves space).
    * Instant logs show optimization:
        Ensure stdout/stderr is unbuffered (e.g. logs show up immediately, not in some time or even after container stopped)
        ```Dockerfile
        ENV PYTHONUNBUFFERED=1
        ```
        Ensures logs show up in real-time (great for Docker logs)
    * Clean requirements installation, each time using `--no-cache-dir`:
        ```Dockerfile
        RUN pip install --no-cache-dir -r requirements.txt
        ```
    * Space optimization: Clean up `__pycache__`
        Cleans up any bytecode just in case something generates it during copy or install.
        ```Dockerfile
        RUN find . -type d -name '__pycache__' -exec rm -rf {} +
        ```
        > Note:
        > Why do this if PYTHONDONTWRITEBYTECODE=1 is set?
        > Sometimes tools or scripts (e.g. local dev environments, tests) may have generated .pyc files before we copied them into the container. This command ensures that no stale bytecode files remain in the final image — just in case.
* Separate credentials for different concern users
    Since database management (e.g. using root privileges), web application connected to database to managed available to it databases and pgAdmin connected to database are different concerns, they require different users or different access permissions and better should not be mixed up.
    This was achieved by separating these users into different users with their own credentials (`root db user`, `app user`, `pgAdmin user`), that may be easily set in `.env` file:
    ```env
    # Main superuser credentials for initial DB creation
    DB_ADMIN_USER=postgres
    DB_ADMIN_PASSWORD=your_secret_db_password_here

    # App user (limited) - the user your app will use to access the database
    DB_APP_USER=app_user
    DB_APP_PASSWORD=app_db_secret_password

    # pgAdmin user credentials to access database management
    DB_ADMIN_PANEL_ACCESS_EMAIL=pgadmin@local.dev
    DB_ADMIN_PANEL_PASSWORD=your_secret_pgadmin_password_here
    ```
* Added automatic Postgres database initialization using `.env` file.
    Database is initialized with root user in [./compose.yaml](./compose.yaml) and web application user, script with template for which are located in [init/db/](./init/db/).
    Whole description for this part is located in a separate [Readme file](./init/db/Readme.md).
* Added automatic pgAdmin initialization using `.env` file.
    PgAdmin is automatically added with pgAdmin user and servers information.
    Script and template are located in [init/pgadmin/](./init/pgadmin/). 
    Whole description for this part is located in a separate [Readme file](./init/pgadmin/Readme.md).
* Alpine image for postgres was used in [compose.yaml](./compose.yaml) config file to reduce final image size. Some standard full-size image features may be absent and may require workarounds or additional installation.
* To enhance security, by default direct access to database using it's port is turned off. Access to database should be done using provided pgAdmin tool.
    Direct access to database still may be turned on by uncommenting line with `DB_PORT` variable in `.env` file:
    ```env
    # DB_PORT=5432  # Commented for better security and access via pgAdmin tool only.
    ```
    and uncommenting port forward for `db` service in [compose.yaml](./compose.yaml) config file:
    ```yaml
    # ports:
    # - "${DB_PORT:-5432}:5432" # Commented for better security and access via pgAdmin tool only.
    ```
    Then you may have direct access to database using db client of you choice.

#### Fixes

#### Potential future improvements

* **Development vs Production Dependancies**
    * **Now**:
        Currently all dependencies are located in one common [./requirements.txt](./requirements.txt) file.
    * **Suggestion**:
        Separate project dependencies into two categories `Production Dependencies` and `Dev/Test-Only Dependencies`.
        This will require to separate some dependencies in a separate file `requirements-dev.txt` file. Following `Dev/Test-Only Dependencies` may be substituted from provided [requirements.txt](./requirements.txt) file  and put into separate `requirements-dev.txt`:

        | Package                 | Category    | Reason           |
        | ----------------------- | ----------- | ---------------- |
        | `faker==20.1.0`         | Development | Clearly for generating fake data during testing. |
        | `exceptiongroup==1.2.0` | Development | Only needed in Python < 3.11 for better traceback grouping. In Python 3.10 it's optional and mainly pulled by test tools like `pytest`. |
        | `colorama==0.4.6`       | Development (optional) | Terminal color formatting — typically used in CLI/debug logging. Safe to exclude in production. |
    * **Result**:
        Separated concern for each environment. Smaller production image size, reduced by unnecessary dependencies.
* **Team Development and Production Enviroment**
    Current solution is suitable for local development and some improvements should be done for collaborative development or even use in production, which was out of this project task, but highly recommended.
    * **Separate** `.env.` **files foe each service**:
        * **Now**:
            Current solution is for local development only!
            Using `.env` files to safely hide out environment setting is great for security and CI/CD-friendly.
            But now each service receives common `.env` file for its initialization and operation. And even though these data are hidden in a form of environmental variables inside container itself, each server knows more about other service more than it should. This creates potential security risk if any of services is compromised.
        * **Suggestion**:
            Separate common `.env` files into separate `.env.*` files (e.g. `.env.pgadmin`), even if there will duplicated variables across different files would fix this.
            Separate `.env` file for each production environment (e.g. `.env.web.production`).
        * **Result**:
            Each service and environment receives what it really needs.
            Enhances security in case of access to environmental variables of one of services.
    * **Separate** `compose` **files (or compose override) for each development environment**:
        * **Now**:
            Current solution is for local development only!
            Team Development Environment or Production should have its own [compose](./compose.yaml) configurations for various environments like `development`, `test`, or `production`.
        * **Suggestion**
            It may be reached by overriding the base `compose.yaml` file instruction using
            ```bash
            docker compose -f compose.yaml -f compose.dev.yaml up
            ```
            Or:
            ```bash
            docker compose -f compose.yaml -f compose.prod.yaml up -d
            ```
            Where:
            * `compose.yaml` contains the shared, base configuration.
            * `compose.[env].yaml` contains environment-specific overrides.
        * **Result**:
            This allows you to:
            * Change environment variables
            * Mount different volumes
            * Use different images or commands
            * Control resource limits differently per environment
* **Container management and orchestration**
    * **Now**:
        Manual control of run/stopped containers.
    * **Suggestion**
        As now there is healthchecker available for the running containers, some sort of [Swarm mode](https://docs.docker.com/engine/swarm/) or tools like [Kubernetes](https://kubernetes.io/) for management of containerized applications may be used.
    * **Result**:
        Automatic track of containers status and their restart if something wend wrong and contained marked as `unhealthy`

## Project Setup & Run Instructions

This guide will help you set up the development environment and run the project.

### Prerequisites

Before you begin, make sure you have the following installed:

* **[Python 3.10.*](https://www.python.org/downloads/release/python-31018/)** (tested with 3.10.18) — Required to run the FastAPI application locally (outside Docker, if needed).
* **[Docker](https://www.docker.com/)** — Used to containerize the application, PostgreSQL database, and pgAdmin in a unified environment using Docker Compose.
* (Optional) **[Git](https://git-scm.com/downloads)** — To clone [the repository](https://github.com/oleksandr-romashko/goit-pythonweb-hw-02), version control and development.
* (Optional: Developemnt) **[VS Code](https://code.visualstudio.com/download)** or another IDE — Recommended for browsing and editing the project source code and overall development.
* (Optional) **[pyenv](https://github.com/pyenv/pyenv)** - Used to set version of Python during development (tested with pyenv version 2.6.1).

### Setting Up the Development Environment

#### 1. Clone the Repository

```bash
git clone https://github.com/oleksandr-romashko/goit-pythonweb-hw-02.git
cd goit-pythonweb-hw-02-main
```

or download the ZIP archive from [GitHub Repository](https://github.com/oleksandr-romashko/goit-pythonweb-hw-02) and extract it.

#### 2. Choose Setup Method

You can either run the project in a fully containerized development environment (**_recommended_**) or set it up locally using a virtual environment.

##### 🐳 Option 1: Using Docker (_Recommended_)

> This method runs the FastAPI app, PostgreSQL database, and pgAdmin in a single Docker Compose network.

1. **Make a copy out of** [.env.example](.env.example) **and name it ** `.env`**. Adjust the values to configure the application and related containers (first of all passwords, maybe ports).**
   Example of `.env` file, shown in [.env.example](./.env.example):
    ```env
    # === WEB PORTAL SETTINGS ===

    WEB_PORT=8000

    # === DATABASE SETTINGS AND CREDENTIALS ===

    DB_NAME=mydb
    DB_HOST=hw02db
    # DB_PORT=5432  # Commented for better security and access via pgAdmin tool only.

    # Main superuser credentials for initial DB creation
    DB_ADMIN_USER=postgres  # It is recommended to leave default value to prevent issues with services
    DB_ADMIN_PASSWORD=your_db_root_user_secret_password_here

    # App user (limited) - the user your app will use to access the database
    DB_APP_USER=app_user
    DB_APP_PASSWORD=your_app_accessing_db_limited_user_secret_password

    # === DATABASE ADMIN PANEL ===
    # DB_ADMIN_PANEL_* is used only to log into pgAdmin (admin interface)

    # pgAdmin user credentials to access database management
    DB_ADMIN_PANEL_ACCESS_EMAIL=pgadmin@local.dev
    DB_ADMIN_PANEL_PASSWORD=your_pgadmin_user_secret_password_here

    DB_ADMIN_PANEL_PORT=5050
   ```
   
   > ⚠️ It is highly recommended to set strong, distinct passwords for:
   > * `DB_ADMIN_PASSWORD` (password for database admin user)
   > * `DB_APP_PASSWORD` (password for the user with limited permissions, created specifically for application accessing database)
   > * `DB_ADMIN_PANEL_PASSWORD` (password for pgAdmin panel user access to manage database).
   
   > ℹ️ 🔓 To expose the PostgreSQL port (e.g., for connection from external tools), uncomment the line:
   > `# DB_PORT=5432`
2. **Start the Environment:**
    _(with optional `tools` profile to start pgAdmin if needed)_
    ```bash
    docker compose --profile tools up
    ```
    This will:
    1. Download all necessary image dependencies.
    2. Build the `FastAPI` app image and run container.
    3. Initialize and start `PostgreSQL` and `pgAdmin` containers with values in .env file.
    5. Expose:
        * FastAPI app at: [localhost:8000](http://localhost:8000) (default port is set by `WEB_PORT` in `.env`)
        * pgAdmin at: [localhost:5050](http://localhost:5050) (default port is set by `DB_ADMIN_PANEL_PORT` in `.env`)
        * PostgreSQL database is not exposed by default(may be configured in the .env file - uncomment line with `DB_PORT` in `.env` to expose it)
3. **Shut Down:**
    ```bash
    docker compose down
    ```

##### 🐍 Option 2: Local Virtual Environment

Use this method if you want to run the FastAPI app locally (without containers).

1. **Create and Activate Virtual Environment**
    _(Use venv, poetry, or your preferred tool)_
    On Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    On Windows:
    ```bash
    python -m venv venv 
    venv\Scripts\activate
    ```
2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. Run the FastAPI App Locally
    ```bash
    python ./src/main.py
    ```

    > ⚠️ You will still need access to a running PostgreSQL database for the application to function. Make sure the database configuration in your `.env` file is valid (e.g., pointing to your local or external DB).
