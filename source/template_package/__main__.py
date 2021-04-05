import logging
import template_package.config.config as con

from template_package.config.config import Config
from template_package.config.script_exit_code import ScriptExitCode


def main():
    script_exit_code = ScriptExitCode.OK
    config = Config()
    logging.debug('Parsed args: %s.', repr(config.args))
    logging.debug('Mode: %s.', config.args.mode)
    logging.info('Parameter provided as command line argument: log_level=%s.', config.args.log_level)
    logging.info('Parameter provided as command line argument: basic_param=%s.', config.args.basic_param)
    logging.info('Parameter provided as command line argument: common_int_param=%s.', config.args.common_int_param)
    config.args.common_int_param = 45
    print(config.args.__dict__)
    logging.info('A new value of "common_int_param" argument is "%s"', config.args.common_int_param)
    logging.info('Is common_int_param also a integer? - %s!', isinstance(config.args.common_int_param, int))
    logging.info('Parameter provided as command line argument: common_list_param=%s.', config.args.common_list_param)
    logging.info('The last element of the list: %s.', config.args.common_list_param[-1])
    append_element = 'last'
    logging.info('Appending "%s" to the list...', append_element)
    config.args.common_list_param.append(append_element)
    logging.info('Subsequent elements of the list:')
    for i, j in enumerate(config.args.common_list_param):
        print(i, j)
    logging.info('Parameter provided as command line argument: a_mode_param=%s.', config.args.a_mode_param)
    logging.info('Is a_mode_param also a string? - %s!', isinstance(config.args.a_mode_param, str))
    if script_exit_code != ScriptExitCode.OK:
        logging.error('%s', script_exit_code.message)
    else:
        logging.info('%s', script_exit_code.message)
    logging.info('Script exiting with an error code: %s.', script_exit_code.code)


if __name__ == '__main__':
    main()
