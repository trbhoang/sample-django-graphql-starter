from ariadne import (
    QueryType,
    MutationType,
    ScalarType,
    make_executable_schema,
    load_schema_from_path,
    snake_case_fallback_resolvers
)
import os
import dateutil


from .user.resolvers import (
    resolve_user,
    resolve_users,
    resolve_create_user,
)


datetime_scalar = ScalarType("DateTime")


@datetime_scalar.serializer
def serialize_datetime(value):
    return value.isoformat()


@datetime_scalar.value_parser
def parse_datetime_value(value):
    if value:
        return dateutil.parser.parse(value)


@datetime_scalar.literal_parser
def parse_datetime_literal(ast):
    value = str(ast.value)
    return parse_datetime_value(value)


type_defs = load_schema_from_path(os.path.join(
    os.path.dirname(__file__), 'schema.graphql'))

query = QueryType()
query.set_field("user", resolve_user)
query.set_field("users", resolve_users)

mutation = MutationType()
mutation.set_field("createUser", resolve_create_user)

schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers)
