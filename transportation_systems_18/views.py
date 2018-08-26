from civic_sandbox.map_layer_maker import SandboxMaker 


safety_hotline_layer = SandboxMaker(
    layer_key = 'transportation_systems_18_001',
    )

sensors_layer = SandboxMaker(
    layer_key = 'transportation_systems_18_002',
    )


crashes_layer = SandboxMaker(
    layer_key = 'transportation_systems_18_003',
    )

route_change_layer = SandboxMaker(
    layer_key = 'transportation_systems_18_004',
    )

block_change_layer = SandboxMaker(
    layer_key = 'transportation_systems_18_005',
    )
