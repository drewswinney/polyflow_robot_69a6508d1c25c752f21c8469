import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a651a51c25c752f21c84a0",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a651a51c25c752f21c84a0",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a651c21c25c752f21c84c9","source_node_id":"69a651c01c25c752f21c84c6","source_pin_id":"front_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a651af1c25c752f21c84b4",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a651af1c25c752f21c84b4",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a651c41c25c752f21c84cc","source_node_id":"69a651c01c25c752f21c84c6","source_pin_id":"rear_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a651b41c25c752f21c84ba",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a651b41c25c752f21c84ba",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a651c51c25c752f21c84cf","source_node_id":"69a651c01c25c752f21c84c6","source_pin_id":"front_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a651b91c25c752f21c84c0",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a651b91c25c752f21c84c0",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a651c71c25c752f21c84d2","source_node_id":"69a651c01c25c752f21c84c6","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="differential_drive",
            executable="differential_drive_node",
            name="differential_drive_69a651c01c25c752f21c84c6",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a651c01c25c752f21c84c6",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"wheel_radius":0.05,"wheel_separation":0.3,"max_wheel_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c8e4b3f393789aad6f84:cmd_vel","name":"cmd_vel","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3c8e4b3f393789aad6f84:mode","name":"mode","direction":"input","msg_type":"polyflow_msgs/ModeState"},{"pin_id":"69a3c8e4b3f393789aad6f84:encoder_left","name":"encoder_left","direction":"input","msg_type":"polyflow_msgs/EncoderState"},{"pin_id":"69a3c8e4b3f393789aad6f84:encoder_right","name":"encoder_right","direction":"input","msg_type":"polyflow_msgs/EncoderState"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_left_motor","name":"front_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_left_motor","name":"rear_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_right_motor","name":"front_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_right_motor","name":"rear_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:odometry","name":"odometry","direction":"output","msg_type":"nav_msgs/Odometry"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a651ce1c25c752f21c84dc","source_node_id":"69a651cb1c25c752f21c84d8","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"},{"connection_id":"69a651d71c25c752f21c84e6","source_node_id":"69a651d41c25c752f21c84e2","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"},{"connection_id":"69a651df1c25c752f21c84ef","source_node_id":"69a651db1c25c752f21c84eb","source_pin_id":"mode","target_pin_id":"mode"},{"connection_id":"69a651e41c25c752f21c84f7","source_node_id":"69a651e21c25c752f21c84f4","source_pin_id":"encoder_state","target_pin_id":"encoder_left"},{"connection_id":"69a651e81c25c752f21c84ff","source_node_id":"69a651e61c25c752f21c84fc","source_pin_id":"encoder_state","target_pin_id":"encoder_right"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a651c21c25c752f21c84c9","target_node_id":"69a651a51c25c752f21c84a0","source_pin_id":"front_left_motor","target_pin_id":"command"},{"connection_id":"69a651c41c25c752f21c84cc","target_node_id":"69a651af1c25c752f21c84b4","source_pin_id":"rear_left_motor","target_pin_id":"command"},{"connection_id":"69a651c51c25c752f21c84cf","target_node_id":"69a651b41c25c752f21c84ba","source_pin_id":"front_right_motor","target_pin_id":"command"},{"connection_id":"69a651c71c25c752f21c84d2","target_node_id":"69a651b91c25c752f21c84c0","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
            }
        ),
        Node(
            package="gamepad",
            executable="gamepad_node",
            name="gamepad_69a651cb1c25c752f21c84d8",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a651cb1c25c752f21c84d8",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"device_index":0,"poll_rate_hz":60,"deadzone":0.05,"max_linear_speed":1,"max_angular_speed":2}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":60,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c77bb3f393789aad6f62:axes","name":"axes","direction":"output","msg_type":"polyflow_msgs/GamepadAxes"},{"pin_id":"69a3c77bb3f393789aad6f62:buttons","name":"buttons","direction":"output","msg_type":"polyflow_msgs/GamepadButtons"},{"pin_id":"69a3c77bb3f393789aad6f62:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a651ce1c25c752f21c84dc","target_node_id":"69a651c01c25c752f21c84c6","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
        Node(
            package="mission_runner",
            executable="mission_runner_node",
            name="mission_runner_69a651d41c25c752f21c84e2",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a651d41c25c752f21c84e2",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"mission":[],"linear_speed":0.5,"angular_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":10,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a477bcc85549d8e55e27db:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a477bcc85549d8e55e27db:status","name":"status","direction":"output","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a651d71c25c752f21c84e6","target_node_id":"69a651c01c25c752f21c84c6","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
        Node(
            package="mode_switcher",
            executable="mode_switcher_node",
            name="mode_switcher_69a651db1c25c752f21c84eb",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a651db1c25c752f21c84eb",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"default_mode":"stopped","allowed_modes":["teleop","automated","stopped"]}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd36b3f393789aad7079:set_mode","name":"set_mode","direction":"input","msg_type":"polyflow_msgs/ModeCommand"},{"pin_id":"69a3cd36b3f393789aad7079:mode","name":"mode","direction":"output","msg_type":"polyflow_msgs/ModeState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a651df1c25c752f21c84ef","target_node_id":"69a651c01c25c752f21c84c6","source_pin_id":"mode","target_pin_id":"mode"}]')),
            }
        ),
        Node(
            package="optical_encoder",
            executable="optical_encoder_node",
            name="optical_encoder_69a651e21c25c752f21c84f4",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a651e21c25c752f21c84f4",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"encoder_id":"encoder_0","ticks_per_rev":1024,"publish_rate_hz":50}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c932b3f393789aad6fbc:reset","name":"reset","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3c932b3f393789aad6fbc:encoder_state","name":"encoder_state","direction":"output","msg_type":"polyflow_msgs/EncoderState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a651e41c25c752f21c84f7","target_node_id":"69a651c01c25c752f21c84c6","source_pin_id":"encoder_state","target_pin_id":"encoder_left"}]')),
            }
        ),
        Node(
            package="optical_encoder",
            executable="optical_encoder_node",
            name="optical_encoder_69a651e61c25c752f21c84fc",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a651e61c25c752f21c84fc",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"encoder_id":"encoder_0","ticks_per_rev":1024,"publish_rate_hz":50}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c932b3f393789aad6fbc:reset","name":"reset","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3c932b3f393789aad6fbc:encoder_state","name":"encoder_state","direction":"output","msg_type":"polyflow_msgs/EncoderState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a651e81c25c752f21c84ff","target_node_id":"69a651c01c25c752f21c84c6","source_pin_id":"encoder_state","target_pin_id":"encoder_right"}]')),
            }
        ),
    ])