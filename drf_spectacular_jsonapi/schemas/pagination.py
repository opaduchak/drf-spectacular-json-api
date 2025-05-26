from rest_framework_json_api.pagination import JsonApiPageNumberPagination


class JsonApiPageNumberPagination(JsonApiPageNumberPagination):

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'meta': {
                    'type': 'object',
                    'properties': {
                        'pagination': {
                            'type': 'object',
                            'properties': {
                                'page': {
                                    'type': 'integer',
                                    'example': 1
                                },
                                'pages': {
                                    'type': 'integer',
                                    'example':1
                                },
                                'count': {
                                    'type': 'integer',
                                    'example': 2
                                },
                            },
                            'required': ['count', 'next', 'prev']
                        }
                    },
                    'required': ['pagination']
                },
                'data': schema,
                'links': {
                    'type': 'object',
                    'properties': {
                        'first': {
                            'type': 'string',
                            'nullable': True,
                            'format': 'uri',
                            'example': f'http://api.example.org/accounts/?{self.page_query_param}=1'
                        },
                        'last': {
                            'type': 'string',
                            'nullable': True,
                            'format': 'uri',
                            'example': f'http://api.example.org/accounts/?{self.page_query_param}=3'
                        },
                        'next': {
                            'type': 'string',
                            'nullable': True,
                            'format': 'uri',
                            'example': f'http://api.example.org/accounts/?{self.page_query_param}=3'
                        },
                        'prev': {
                            'type': 'string',
                            'nullable': True,
                            'format': 'uri',
                            'example': f'http://api.example.org/accounts/?{self.page_query_param}=1'
                        },
                    },
                    'required': ['count', 'next', 'prev']
                }
            },
            'required': ['meta', 'data', 'links']
        }
