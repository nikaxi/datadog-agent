# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

import hashlib

# list of fixture names
FIXTURE_LIST = [
    '_api_class_eqptcapacityEntity_json_query_target_self_rsp_subtree_include_stats_rsp_subtree_class_eqptcapacityL3TotalUsage5min',
    '_api_class_eqptcapacityEntity_json_query_target_self_rsp_subtree_include_stats_rsp_subtree_class_eqptcapacityL3TotalUsageCap5min',
    '_api_class_eqptcapacityEntity_json_query_target_self_rsp_subtree_include_stats_rsp_subtree_class_eqptcapacityMcastUsage5min',
    '_api_class_eqptcapacityEntity_json_query_target_self_rsp_subtree_include_stats_rsp_subtree_class_eqptcapacityPolUsage5min',
    '_api_class_eqptcapacityEntity_json_query_target_self_rsp_subtree_include_stats_rsp_subtree_class_eqptcapacityVlanUsage5min',
    '_api_class_fabricNode_json_query_target_filter_eq_fabricNode_role__leaf__',
    '_api_class_fvAEPg_json_rsp_subtree_include_count',
    '_api_class_fvBD_json_rsp_subtree_include_count',
    '_api_class_fvCEp_json_rsp_subtree_include_count',
    '_api_class_fvCtx_json_rsp_subtree_include_count',
    '_api_class_fvTenant_json_rsp_subtree_include_count',
    '_api_mo_topology_json_query_target_subtree_target_subtree_class_fabricNode',
    '_api_mo_topology_json_query_target_subtree_target_subtree_class_fabricPod',
    '_api_mo_topology_pod_1_json_rsp_subtree_include_stats_no_scoped_page_size_20',
    '_api_mo_topology_pod_1_node_101_sys_json_query_target_subtree_target_subtree_class_l1PhysIf',
    '_api_mo_topology_pod_1_node_101_sys_json_rsp_subtree_include_stats_no_scoped_page_size_20',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_10__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_11__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_12__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_13__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_14__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_15__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_16__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_17__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_18__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_19__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_1__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_20__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_21__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_22__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_23__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_24__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_25__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_26__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_27__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_28__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_29__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_2__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_30__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_31__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_32__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_33__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_34__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_35__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_36__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_37__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_38__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_39__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_3__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_40__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_41__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_42__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_43__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_44__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_45__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_46__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_47__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_48__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_4__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_5__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_6__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_7__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_8__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth101_1_9__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_10__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_11__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_12__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_13__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_14__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_15__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_16__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_17__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_18__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_19__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_1__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_20__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_21__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_22__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_23__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_24__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_25__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_26__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_27__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_28__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_29__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_2__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_30__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_31__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_32__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_33__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_34__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_35__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_36__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_37__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_38__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_39__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_3__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_40__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_41__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_42__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_43__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_44__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_45__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_46__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_47__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_48__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_49__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_4__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_50__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_51__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_52__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_53__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_54__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_5__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_6__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_7__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_8__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_101_sys_phys__eth1_9__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_json_query_target_subtree_target_subtree_class_l1PhysIf',
    '_api_mo_topology_pod_1_node_102_sys_json_rsp_subtree_include_stats_no_scoped_page_size_20',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_10__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_11__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_12__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_13__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_14__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_15__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_16__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_17__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_18__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_19__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_1__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_20__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_21__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_22__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_23__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_24__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_25__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_26__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_27__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_28__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_29__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_2__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_30__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_31__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_32__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_33__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_34__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_35__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_36__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_37__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_38__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_39__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_3__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_40__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_41__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_42__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_43__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_44__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_45__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_46__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_47__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_48__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_49__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_4__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_50__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_51__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_52__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_53__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_54__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_5__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_6__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_7__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_8__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_102_sys_phys__eth1_9__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_json_query_target_subtree_target_subtree_class_l1PhysIf',
    '_api_mo_topology_pod_1_node_201_sys_json_rsp_subtree_include_stats_no_scoped_page_size_20',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_10__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_11__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_12__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_13__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_14__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_15__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_16__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_17__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_18__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_19__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_1__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_20__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_21__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_22__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_23__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_24__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_25__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_26__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_27__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_28__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_29__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_2__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_30__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_31__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_32__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_33__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_34__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_35__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_36__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_3__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_4__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_5__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_6__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_7__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_8__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_201_sys_phys__eth1_9__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_json_query_target_subtree_target_subtree_class_l1PhysIf',
    '_api_mo_topology_pod_1_node_202_sys_json_rsp_subtree_include_stats_no_scoped_page_size_20',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_10__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_11__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_12__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_13__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_14__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_15__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_16__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_17__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_18__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_19__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_1__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_20__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_21__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_22__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_23__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_24__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_25__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_26__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_27__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_28__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_29__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_2__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_30__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_31__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_32__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_33__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_34__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_35__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_36__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_3__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_4__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_5__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_6__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_7__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_8__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_topology_pod_1_node_202_sys_phys__eth1_9__json_rsp_subtree_include_stats_no_scoped_page_size_50',
    '_api_mo_uni_fabric_compcat_default_fvsw_default_capabilities_json_query_target_children_target_subtree_class_fvcapRule',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_Ecomm_json_query_target_subtree_target_subtree_class_fvCEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_Ecomm_json_query_target_subtree_target_subtree_class_fvRsCEpToPathEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_Ecomm_json_rsp_subtree_include_stats_no_scoped',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_Inv_json_query_target_subtree_target_subtree_class_fvCEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_Inv_json_query_target_subtree_target_subtree_class_fvRsCEpToPathEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_Inv_json_rsp_subtree_include_stats_no_scoped',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_MiscAppVMs_json_query_target_subtree_target_subtree_class_fvCEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_MiscAppVMs_json_query_target_subtree_target_subtree_class_fvRsCEpToPathEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_MiscAppVMs_json_rsp_subtree_include_stats_no_scoped',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_Ord_json_query_target_subtree_target_subtree_class_fvCEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_Ord_json_query_target_subtree_target_subtree_class_fvRsCEpToPathEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_Ord_json_rsp_subtree_include_stats_no_scoped',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_Pay_json_query_target_subtree_target_subtree_class_fvCEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_Pay_json_query_target_subtree_target_subtree_class_fvRsCEpToPathEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_epg_DtDg_Pay_json_rsp_subtree_include_stats_no_scoped',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_json_query_target_subtree_target_subtree_class_fvAEPg',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP1_EcommerceApp_json_rsp_subtree_include_stats_no_scoped',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP2_Jeti_epg_DtDg_Jeti1_json_query_target_subtree_target_subtree_class_fvCEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP2_Jeti_epg_DtDg_Jeti1_json_query_target_subtree_target_subtree_class_fvRsCEpToPathEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP2_Jeti_epg_DtDg_Jeti1_json_rsp_subtree_include_stats_no_scoped',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP2_Jeti_epg_DtDg_Jeti2_json_query_target_subtree_target_subtree_class_fvCEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP2_Jeti_epg_DtDg_Jeti2_json_query_target_subtree_target_subtree_class_fvRsCEpToPathEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP2_Jeti_epg_DtDg_Jeti2_json_rsp_subtree_include_stats_no_scoped',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP2_Jeti_epg_DtDg_Jetty_Controller_json_query_target_subtree_target_subtree_class_fvCEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP2_Jeti_epg_DtDg_Jetty_Controller_json_query_target_subtree_target_subtree_class_fvRsCEpToPathEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP2_Jeti_epg_DtDg_Jetty_Controller_json_rsp_subtree_include_stats_no_scoped',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP2_Jeti_json_query_target_subtree_target_subtree_class_fvAEPg',
    '_api_mo_uni_tn_DataDog_ap_DtDg_AP2_Jeti_json_rsp_subtree_include_stats_no_scoped',
    '_api_mo_uni_tn_DataDog_ap_DtDg_test_AP_epg_Test_EPG_json_query_target_subtree_target_subtree_class_fvCEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_test_AP_epg_Test_EPG_json_query_target_subtree_target_subtree_class_fvRsCEpToPathEp',
    '_api_mo_uni_tn_DataDog_ap_DtDg_test_AP_epg_Test_EPG_json_rsp_subtree_include_stats_no_scoped',
    '_api_mo_uni_tn_DataDog_ap_DtDg_test_AP_json_query_target_subtree_target_subtree_class_fvAEPg',
    '_api_mo_uni_tn_DataDog_ap_DtDg_test_AP_json_rsp_subtree_include_stats_no_scoped',
    '_api_mo_uni_tn_DataDog_json_query_target_subtree_target_subtree_class_fvAp',
    '_api_mo_uni_tn_DataDog_json_rsp_subtree_include_stats_no_scoped',
    '_api_node_class_ctxClassCnt_json_rsp_subtree_class_fvEpP',
    '_api_node_class_ctxClassCnt_json_rsp_subtree_class_l2BD',
    '_api_node_class_ctxClassCnt_json_rsp_subtree_class_l3Dom',
    '_api_node_mo_topology_pod_1_node_101_sys_procsys_json_rsp_subtree_include_stats_no_scoped_rsp_subtree_class_procSysMemHist5min_procSysCPUHist5min',
    '_api_node_mo_topology_pod_1_node_102_sys_procsys_json_rsp_subtree_include_stats_no_scoped_rsp_subtree_class_procSysMemHist5min_procSysCPUHist5min',
    '_api_node_mo_topology_pod_1_node_1_sys_proc_json_rsp_subtree_include_stats_no_scoped_rsp_subtree_class_procMemHist5min_procCPUHist5min',
    '_api_node_mo_topology_pod_1_node_201_sys_procsys_json_rsp_subtree_include_stats_no_scoped_rsp_subtree_class_procSysMemHist5min_procSysCPUHist5min',
    '_api_node_mo_topology_pod_1_node_202_sys_procsys_json_rsp_subtree_include_stats_no_scoped_rsp_subtree_class_procSysMemHist5min_procSysCPUHist5min',
    '_api_node_mo_topology_pod_1_node_2_sys_proc_json_rsp_subtree_include_stats_no_scoped_rsp_subtree_class_procMemHist5min_procCPUHist5min',
    '_api_node_mo_topology_pod_1_node_3_sys_proc_json_rsp_subtree_include_stats_no_scoped_rsp_subtree_class_procMemHist5min_procCPUHist5min',
    '_api_node_mo_uni_tn_DataDog_json_rsp_subtree_include_event_logs_no_scoped_subtree_order_by_eventRecord_created_desc_page_0_page_size_15',
]


# The map will contain the md5 hash to the fixture
# name. The file on disk should be named with the
# {MD5 hash}.txt of the mock_path used.
FIXTURE_LIST_FILE_MAP = {}
for fixture in FIXTURE_LIST:
    FIXTURE_LIST_FILE_MAP[fixture] = hashlib.md5(fixture).hexdigest()
