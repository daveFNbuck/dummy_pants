python_binary(
    name='load_pkg',
    source='load_pkg.py',
    dependencies=[
        'src/python/mod',
        'src/python/mod/submod',
        'src/python/mod/submod/subsubmod',
    ],
)

python_requirement_library(
    name='protobuf',
    requirements=[
        python_requirement('protobuf'),
    ]
)

python_requirement_library(
    name='snakebite',
    requirements=[
        python_requirement('snakebite==2.11.0'),
    ]
)

python_binary(
    name='protobuf_version',
    source='protobuf_version.py',
    dependencies=[
        ':protobuf',
    ]
)

python_binary(
    name='protobuf_version2',
    source='protobuf_version.py',
    dependencies=[
        ':snakebite',
    ]
)
