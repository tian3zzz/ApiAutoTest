from config import log_config
import logging


# 相等
def equals(actual, expect):
    assert actual == expect


# 不等于
def not_equals(actual, expect):
    assert actual != expect


# 大于
def greater_than(actual, expect):
    assert actual > expect


# 大于或等于
def greater_than_or_equals(actual, expect):
    assert actual >= expect


# 小于
def less_than(actual, expect):
    assert actual < expect


# 小于或等于
def less_than_or_equals(actual, expect):
    assert actual <= expect


# 是否为空
def is_null(actual):
    assert actual is None


# 是否不为空
def is_not_null(actual):
    assert actual is not None

