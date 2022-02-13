from .jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    unique_types = set([
        job['job_type'] for job in jobs
    ])
    return list(unique_types)


def filter_by_job_type(jobs, job_type):
    jobs_by_type = [
        job for job in jobs if job['job_type'] == job_type
    ]

    return jobs_by_type


def get_unique_industries(path):
    jobs = read(path)
    unique_industries = set([
        job['industry'] for job in jobs if job['industry']
    ])
    return list(unique_industries)


def filter_by_industry(jobs, industry):
    jobs_by_industry = [
        job for job in jobs if job['industry'] == industry
    ]

    return jobs_by_industry


def get_max_salary(path):
    jobs = read(path)

    max_salary = max([
        int(job["max_salary"])
        for job in jobs
        if job["max_salary"].isdigit()
    ])

    return max_salary


def get_min_salary(path):
    jobs = read(path)

    min_salary = min([
        int(job["min_salary"])
        for job in jobs
        if job["min_salary"].isdigit()
    ])

    return min_salary


def matches_salary_range(job, salary):
    if (
        'max_salary' not in job or
        'min_salary' not in job
    ):
        raise ValueError('"job must have "max_salary" and "min_salary" keys')

    if (
        type(job['max_salary']) != int or
        type(job['min_salary']) != int or
        type(salary) != int
    ):
        raise ValueError(
            '"max_salary" and "min_salary" keys and "salary" must be numbers'
        )

    if (
        job['min_salary'] > job['max_salary']
    ):
        raise ValueError(
            '"min_salary" must be less then "max_salary"'
        )

    return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass

    return filtered_jobs
