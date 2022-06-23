import subprocess
from shlex import quote

import click


@click.command()
@click.argument('filepath')
@click.option('--binpath', default='', help='Путь до исполняемых файлов.')
def main(filepath: str, binpath: str = ''):
    """Скрипт для реализации пайплайна автоформатирования.

    Отображается вывод результатов от самих плагинов.

    :param filepath: путь до файла.
    :param binpath: путь для расположения плагинов автоформатирования.
    """
    ordered_formatters = (
        (
            'autoflake',
            ('--in-place', '--remove-unused-variables', '--remove-all-unused-imports', '--expand-star-imports'),
        ),
        ('docformatter', ('--in-place', '--wrap-summaries 120', '--wrap-descriptions 120')),
        ('unify', ('--in-place',)),
        ('autopep8', ()),
        ('add-trailing-comma', ()),
        ('isort', ()),
    )
    view_length = 20
    bin_path = quote(binpath)
    file_path = quote(filepath)
    for formatter_name, formatter_args in ordered_formatters:
        print('-' * view_length)
        print(formatter_name)
        formatter_args = ' '.join(formatter_args)
        formatter: str = '{formatter_name} {file_path} {formatter_args}'.format(
            formatter_name=formatter_name,
            file_path=file_path,
            formatter_args=formatter_args,
        )
        if binpath:
            formatter: str = '{bin_path}/{formatter}'.format(bin_path=bin_path, formatter=formatter)

        with subprocess.Popen(
            formatter,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            encoding='utf-8',
            universal_newlines=True,
        ) as process:
            while process.poll() is None:
                print(process.stdout.readline(), flush=True)


if __name__ == '__main__':
    main()
