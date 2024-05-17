# encoding: utf-8
# module panda3d.bullet
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\bullet.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .BulletBodyNode import BulletBodyNode

class BulletSoftBodyNode(BulletBodyNode):
    """
    /**
     *
     */
    """
    def addForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_force(const BulletSoftBodyNode self, const LVector3f force)
        add_force(const BulletSoftBodyNode self, const LVector3f force, int node)
        
        // Force
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def addVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_velocity(const BulletSoftBodyNode self, const LVector3f velocity)
        add_velocity(const BulletSoftBodyNode self, const LVector3f velocity, int node)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def add_force(self, const_BulletSoftBodyNode_self, const_LVector3f_force): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_force(const BulletSoftBodyNode self, const LVector3f force)
        add_force(const BulletSoftBodyNode self, const LVector3f force, int node)
        
        // Force
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def add_velocity(self, const_BulletSoftBodyNode_self, const_LVector3f_velocity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_velocity(const BulletSoftBodyNode self, const LVector3f velocity)
        add_velocity(const BulletSoftBodyNode self, const LVector3f velocity, int node)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def appendAnchor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_anchor(const BulletSoftBodyNode self, int node, BulletRigidBodyNode body)
        append_anchor(const BulletSoftBodyNode self, int node, BulletRigidBodyNode body, const LVector3f pivot, bool disable)
        append_anchor(const BulletSoftBodyNode self, int node, BulletRigidBodyNode body, bool disable)
        
        // Anchors
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def appendAngularJoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_angular_joint(const BulletSoftBodyNode self, BulletBodyNode body, const LVector3f axis, float erp, float cfm, float split, BulletSoftBodyControl control)
        
        /**
         *
         */
        """
        pass

    def appendLinearJoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_linear_joint(const BulletSoftBodyNode self, BulletBodyNode body, const LPoint3f pos, float erp, float cfm, float split)
        append_linear_joint(const BulletSoftBodyNode self, BulletBodyNode body, int cluster, float erp, float cfm, float split)
        
        // Links
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def appendMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_material(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def append_anchor(self, const_BulletSoftBodyNode_self, int_node, BulletRigidBodyNode_body): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_anchor(const BulletSoftBodyNode self, int node, BulletRigidBodyNode body)
        append_anchor(const BulletSoftBodyNode self, int node, BulletRigidBodyNode body, const LVector3f pivot, bool disable)
        append_anchor(const BulletSoftBodyNode self, int node, BulletRigidBodyNode body, bool disable)
        
        // Anchors
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def append_angular_joint(self, const_BulletSoftBodyNode_self, BulletBodyNode_body, const_LVector3f_axis, float_erp, float_cfm, float_split, BulletSoftBodyControl_control): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_angular_joint(const BulletSoftBodyNode self, BulletBodyNode body, const LVector3f axis, float erp, float cfm, float split, BulletSoftBodyControl control)
        
        /**
         *
         */
        """
        pass

    def append_linear_joint(self, const_BulletSoftBodyNode_self, BulletBodyNode_body, const_LPoint3f_pos, float_erp, float_cfm, float_split): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_linear_joint(const BulletSoftBodyNode self, BulletBodyNode body, const LPoint3f pos, float erp, float cfm, float split)
        append_linear_joint(const BulletSoftBodyNode self, BulletBodyNode body, int cluster, float erp, float cfm, float split)
        
        // Links
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def append_material(self, const_BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_material(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def clusterCom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        cluster_com(BulletSoftBodyNode self, int cluster)
        
        /**
         *
         */
        """
        pass

    def cluster_com(self, BulletSoftBodyNode_self, int_cluster): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cluster_com(BulletSoftBodyNode self, int cluster)
        
        /**
         *
         */
        """
        pass

    def generateBendingConstraints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        generate_bending_constraints(const BulletSoftBodyNode self, int distance, BulletSoftBodyMaterial material)
        
        /**
         *
         */
        """
        pass

    def generateClusters(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        generate_clusters(const BulletSoftBodyNode self, int k, int maxiterations)
        
        // Cluster
        
        /**
         *
         */
        """
        pass

    def generate_bending_constraints(self, const_BulletSoftBodyNode_self, int_distance, BulletSoftBodyMaterial_material): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate_bending_constraints(const BulletSoftBodyNode self, int distance, BulletSoftBodyMaterial material)
        
        /**
         *
         */
        """
        pass

    def generate_clusters(self, const_BulletSoftBodyNode_self, int_k, int_maxiterations): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate_clusters(const BulletSoftBodyNode self, int k, int maxiterations)
        
        // Cluster
        
        /**
         *
         */
        """
        pass

    def getAabb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_aabb(BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getCfg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cfg(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getClosestNodeIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_closest_node_index(const BulletSoftBodyNode self, LVecBase3f point, bool local)
        
        /**
         * Returns the index of the node which is closest to the given point.  The
         * distance between each node and the given point is computed in world space
         * if local=false, and in local space if local=true.
         */
        """
        pass

    def getMass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mass(BulletSoftBodyNode self, int node)
        
        /**
         *
         */
        """
        pass

    def getMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_material(BulletSoftBodyNode self, int idx)
        
        /**
         *
         */
        """
        pass

    def getMaterials(self, *args, **kwargs): # real signature unknown
        pass

    def getNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node(BulletSoftBodyNode self, int idx)
        
        /**
         *
         */
        """
        pass

    def getNodes(self, *args, **kwargs): # real signature unknown
        pass

    def getNumClusters(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_clusters(BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getNumMaterials(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_materials(BulletSoftBodyNode self)
        
        // Materials
        
        // Materials
        
        // Materials
        
        /**
         *
         */
        """
        pass

    def getNumNodes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_nodes(BulletSoftBodyNode self)
        
        // Nodes
        
        // Nodes
        
        // Nodes
        
        /**
         *
         */
        """
        pass

    def getTotalMass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_mass(BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_volume(BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getWindVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wind_velocity(BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getWorldInfo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_world_info(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_aabb(self, BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_aabb(BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_cfg(self, const_BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cfg(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_closest_node_index(self, const_BulletSoftBodyNode_self, LVecBase3f_point, bool_local): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_closest_node_index(const BulletSoftBodyNode self, LVecBase3f point, bool local)
        
        /**
         * Returns the index of the node which is closest to the given point.  The
         * distance between each node and the given point is computed in world space
         * if local=false, and in local space if local=true.
         */
        """
        pass

    def get_mass(self, BulletSoftBodyNode_self, int_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mass(BulletSoftBodyNode self, int node)
        
        /**
         *
         */
        """
        pass

    def get_material(self, BulletSoftBodyNode_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_material(BulletSoftBodyNode self, int idx)
        
        /**
         *
         */
        """
        pass

    def get_materials(self, *args, **kwargs): # real signature unknown
        pass

    def get_node(self, BulletSoftBodyNode_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node(BulletSoftBodyNode self, int idx)
        
        /**
         *
         */
        """
        pass

    def get_nodes(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_clusters(self, BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_clusters(BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_num_materials(self, BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_materials(BulletSoftBodyNode self)
        
        // Materials
        
        // Materials
        
        // Materials
        
        /**
         *
         */
        """
        pass

    def get_num_nodes(self, BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_nodes(BulletSoftBodyNode self)
        
        // Nodes
        
        // Nodes
        
        // Nodes
        
        /**
         *
         */
        """
        pass

    def get_total_mass(self, BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_mass(BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_volume(self, BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_volume(BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_wind_velocity(self, BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wind_velocity(BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_world_info(self, const_BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_world_info(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def linkCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        link_curve(const BulletSoftBodyNode self, NurbsCurveEvaluator curve)
        
        /**
         *
         */
        """
        pass

    def linkGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        link_geom(const BulletSoftBodyNode self, Geom geom)
        
        // Rendering
        
        /**
         *
         */
        """
        pass

    def linkSurface(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        link_surface(const BulletSoftBodyNode self, NurbsSurfaceEvaluator surface)
        
        /**
         *
         */
        """
        pass

    def link_curve(self, const_BulletSoftBodyNode_self, NurbsCurveEvaluator_curve): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        link_curve(const BulletSoftBodyNode self, NurbsCurveEvaluator curve)
        
        /**
         *
         */
        """
        pass

    def link_geom(self, const_BulletSoftBodyNode_self, Geom_geom): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        link_geom(const BulletSoftBodyNode self, Geom geom)
        
        // Rendering
        
        /**
         *
         */
        """
        pass

    def link_surface(self, const_BulletSoftBodyNode_self, NurbsSurfaceEvaluator_surface): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        link_surface(const BulletSoftBodyNode self, NurbsSurfaceEvaluator surface)
        
        /**
         *
         */
        """
        pass

    def makeEllipsoid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_ellipsoid(BulletSoftBodyWorldInfo info, const LPoint3f center, const LVecBase3f radius, int res)
        
        /**
         *
         */
        """
        pass

    def makePatch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_patch(BulletSoftBodyWorldInfo info, const LPoint3f corner00, const LPoint3f corner10, const LPoint3f corner01, const LPoint3f corner11, int resx, int resy, int fixeds, bool gendiags)
        
        /**
         *
         */
        """
        pass

    def makeRope(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_rope(BulletSoftBodyWorldInfo info, const LPoint3f from, const LPoint3f to, int res, int fixeds)
        
        // Factory
        
        /**
         *
         */
        """
        pass

    def makeTetMesh(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_tet_mesh(BulletSoftBodyWorldInfo info, PointerToArray points, PointerToArray indices)
        make_tet_mesh(BulletSoftBodyWorldInfo info, PointerToArray points, PointerToArray indices, bool tetralinks)
        make_tet_mesh(BulletSoftBodyWorldInfo info, str ele, str face, str node)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def makeTriMesh(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_tri_mesh(BulletSoftBodyWorldInfo info, const Geom geom)
        make_tri_mesh(BulletSoftBodyWorldInfo info, PointerToArray points, PointerToArray indices, bool randomizeConstraints)
        make_tri_mesh(BulletSoftBodyWorldInfo info, const Geom geom, bool randomizeConstraints)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def make_ellipsoid(self, BulletSoftBodyWorldInfo_info, const_LPoint3f_center, const_LVecBase3f_radius, int_res): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_ellipsoid(BulletSoftBodyWorldInfo info, const LPoint3f center, const LVecBase3f radius, int res)
        
        /**
         *
         */
        """
        pass

    def make_patch(self, BulletSoftBodyWorldInfo_info, const_LPoint3f_corner00, const_LPoint3f_corner10, const_LPoint3f_corner01, const_LPoint3f_corner11, int_resx, int_resy, int_fixeds, bool_gendiags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_patch(BulletSoftBodyWorldInfo info, const LPoint3f corner00, const LPoint3f corner10, const LPoint3f corner01, const LPoint3f corner11, int resx, int resy, int fixeds, bool gendiags)
        
        /**
         *
         */
        """
        pass

    def make_rope(self, BulletSoftBodyWorldInfo_info, const_LPoint3f_from, const_LPoint3f_to, int_res, int_fixeds): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_rope(BulletSoftBodyWorldInfo info, const LPoint3f from, const LPoint3f to, int res, int fixeds)
        
        // Factory
        
        /**
         *
         */
        """
        pass

    def make_tet_mesh(self, BulletSoftBodyWorldInfo_info, PointerToArray_points, PointerToArray_indices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_tet_mesh(BulletSoftBodyWorldInfo info, PointerToArray points, PointerToArray indices)
        make_tet_mesh(BulletSoftBodyWorldInfo info, PointerToArray points, PointerToArray indices, bool tetralinks)
        make_tet_mesh(BulletSoftBodyWorldInfo info, str ele, str face, str node)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def make_tri_mesh(self, BulletSoftBodyWorldInfo_info, const_Geom_geom): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_tri_mesh(BulletSoftBodyWorldInfo info, const Geom geom)
        make_tri_mesh(BulletSoftBodyWorldInfo info, PointerToArray points, PointerToArray indices, bool randomizeConstraints)
        make_tri_mesh(BulletSoftBodyWorldInfo info, const Geom geom, bool randomizeConstraints)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def randomizeConstraints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        randomize_constraints(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def randomize_constraints(self, const_BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        randomize_constraints(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def releaseCluster(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_cluster(const BulletSoftBodyNode self, int index)
        
        /**
         *
         */
        """
        pass

    def releaseClusters(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_clusters(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def release_cluster(self, const_BulletSoftBodyNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_cluster(const BulletSoftBodyNode self, int index)
        
        /**
         *
         */
        """
        pass

    def release_clusters(self, const_BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_clusters(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def setMass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mass(const BulletSoftBodyNode self, int node, float mass)
        
        /**
         *
         */
        """
        pass

    def setPose(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pose(const BulletSoftBodyNode self, bool bvolume, bool bframe)
        
        /**
         *
         */
        """
        pass

    def setTotalDensity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_total_density(const BulletSoftBodyNode self, float density)
        
        /**
         *
         */
        """
        pass

    def setTotalMass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_total_mass(const BulletSoftBodyNode self, float mass, bool fromfaces)
        
        /**
         *
         */
        """
        pass

    def setVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_velocity(const BulletSoftBodyNode self, const LVector3f velocity)
        
        /**
         *
         */
        """
        pass

    def setVolumeDensity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_volume_density(const BulletSoftBodyNode self, float density)
        
        /**
         *
         */
        """
        pass

    def setVolumeMass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_volume_mass(const BulletSoftBodyNode self, float mass)
        
        // Mass, volume, density
        
        /**
         *
         */
        """
        pass

    def setWindVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wind_velocity(const BulletSoftBodyNode self, const LVector3f velocity)
        
        /**
         *
         */
        """
        pass

    def set_mass(self, const_BulletSoftBodyNode_self, int_node, float_mass): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mass(const BulletSoftBodyNode self, int node, float mass)
        
        /**
         *
         */
        """
        pass

    def set_pose(self, const_BulletSoftBodyNode_self, bool_bvolume, bool_bframe): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pose(const BulletSoftBodyNode self, bool bvolume, bool bframe)
        
        /**
         *
         */
        """
        pass

    def set_total_density(self, const_BulletSoftBodyNode_self, float_density): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_total_density(const BulletSoftBodyNode self, float density)
        
        /**
         *
         */
        """
        pass

    def set_total_mass(self, const_BulletSoftBodyNode_self, float_mass, bool_fromfaces): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_total_mass(const BulletSoftBodyNode self, float mass, bool fromfaces)
        
        /**
         *
         */
        """
        pass

    def set_velocity(self, const_BulletSoftBodyNode_self, const_LVector3f_velocity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_velocity(const BulletSoftBodyNode self, const LVector3f velocity)
        
        /**
         *
         */
        """
        pass

    def set_volume_density(self, const_BulletSoftBodyNode_self, float_density): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_volume_density(const BulletSoftBodyNode self, float density)
        
        /**
         *
         */
        """
        pass

    def set_volume_mass(self, const_BulletSoftBodyNode_self, float_mass): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_volume_mass(const BulletSoftBodyNode self, float mass)
        
        // Mass, volume, density
        
        /**
         *
         */
        """
        pass

    def set_wind_velocity(self, const_BulletSoftBodyNode_self, const_LVector3f_velocity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wind_velocity(const BulletSoftBodyNode self, const LVector3f velocity)
        
        /**
         *
         */
        """
        pass

    def unlinkCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unlink_curve(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def unlinkGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unlink_geom(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def unlinkSurface(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unlink_surface(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def unlink_curve(self, const_BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unlink_curve(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def unlink_geom(self, const_BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unlink_geom(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def unlink_surface(self, const_BulletSoftBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unlink_surface(const BulletSoftBodyNode self)
        
        /**
         *
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    aabb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cfg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    materials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_clusters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wind_velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    world_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CE870>'
        'aabb': None, # (!) real value is "<attribute 'aabb' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'addForce': None, # (!) real value is "<method 'addForce' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'addVelocity': None, # (!) real value is "<method 'addVelocity' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'add_force': None, # (!) real value is "<method 'add_force' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'add_velocity': None, # (!) real value is "<method 'add_velocity' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'appendAnchor': None, # (!) real value is "<method 'appendAnchor' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'appendAngularJoint': None, # (!) real value is "<method 'appendAngularJoint' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'appendLinearJoint': None, # (!) real value is "<method 'appendLinearJoint' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'appendMaterial': None, # (!) real value is "<method 'appendMaterial' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'append_anchor': None, # (!) real value is "<method 'append_anchor' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'append_angular_joint': None, # (!) real value is "<method 'append_angular_joint' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'append_linear_joint': None, # (!) real value is "<method 'append_linear_joint' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'append_material': None, # (!) real value is "<method 'append_material' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'cfg': None, # (!) real value is "<attribute 'cfg' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'clusterCom': None, # (!) real value is "<method 'clusterCom' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'cluster_com': None, # (!) real value is "<method 'cluster_com' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'generateBendingConstraints': None, # (!) real value is "<method 'generateBendingConstraints' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'generateClusters': None, # (!) real value is "<method 'generateClusters' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'generate_bending_constraints': None, # (!) real value is "<method 'generate_bending_constraints' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'generate_clusters': None, # (!) real value is "<method 'generate_clusters' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getAabb': None, # (!) real value is "<method 'getAabb' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getCfg': None, # (!) real value is "<method 'getCfg' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CE870>)>'
        'getClosestNodeIndex': None, # (!) real value is "<method 'getClosestNodeIndex' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getMass': None, # (!) real value is "<method 'getMass' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getMaterial': None, # (!) real value is "<method 'getMaterial' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getMaterials': None, # (!) real value is "<method 'getMaterials' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getNode': None, # (!) real value is "<method 'getNode' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getNodes': None, # (!) real value is "<method 'getNodes' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getNumClusters': None, # (!) real value is "<method 'getNumClusters' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getNumMaterials': None, # (!) real value is "<method 'getNumMaterials' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getNumNodes': None, # (!) real value is "<method 'getNumNodes' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getTotalMass': None, # (!) real value is "<method 'getTotalMass' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getVolume': None, # (!) real value is "<method 'getVolume' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getWindVelocity': None, # (!) real value is "<method 'getWindVelocity' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'getWorldInfo': None, # (!) real value is "<method 'getWorldInfo' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_aabb': None, # (!) real value is "<method 'get_aabb' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_cfg': None, # (!) real value is "<method 'get_cfg' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CE870>)>'
        'get_closest_node_index': None, # (!) real value is "<method 'get_closest_node_index' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_mass': None, # (!) real value is "<method 'get_mass' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_material': None, # (!) real value is "<method 'get_material' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_materials': None, # (!) real value is "<method 'get_materials' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_node': None, # (!) real value is "<method 'get_node' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_nodes': None, # (!) real value is "<method 'get_nodes' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_num_clusters': None, # (!) real value is "<method 'get_num_clusters' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_num_materials': None, # (!) real value is "<method 'get_num_materials' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_num_nodes': None, # (!) real value is "<method 'get_num_nodes' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_total_mass': None, # (!) real value is "<method 'get_total_mass' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_volume': None, # (!) real value is "<method 'get_volume' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_wind_velocity': None, # (!) real value is "<method 'get_wind_velocity' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'get_world_info': None, # (!) real value is "<method 'get_world_info' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'linkCurve': None, # (!) real value is "<method 'linkCurve' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'linkGeom': None, # (!) real value is "<method 'linkGeom' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'linkSurface': None, # (!) real value is "<method 'linkSurface' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'link_curve': None, # (!) real value is "<method 'link_curve' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'link_geom': None, # (!) real value is "<method 'link_geom' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'link_surface': None, # (!) real value is "<method 'link_surface' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'makeEllipsoid': None, # (!) real value is '<staticmethod(<built-in method makeEllipsoid of type object at 0x00007FFDC68CE870>)>'
        'makePatch': None, # (!) real value is '<staticmethod(<built-in method makePatch of type object at 0x00007FFDC68CE870>)>'
        'makeRope': None, # (!) real value is '<staticmethod(<built-in method makeRope of type object at 0x00007FFDC68CE870>)>'
        'makeTetMesh': None, # (!) real value is '<staticmethod(<built-in method makeTetMesh of type object at 0x00007FFDC68CE870>)>'
        'makeTriMesh': None, # (!) real value is '<staticmethod(<built-in method makeTriMesh of type object at 0x00007FFDC68CE870>)>'
        'make_ellipsoid': None, # (!) real value is '<staticmethod(<built-in method make_ellipsoid of type object at 0x00007FFDC68CE870>)>'
        'make_patch': None, # (!) real value is '<staticmethod(<built-in method make_patch of type object at 0x00007FFDC68CE870>)>'
        'make_rope': None, # (!) real value is '<staticmethod(<built-in method make_rope of type object at 0x00007FFDC68CE870>)>'
        'make_tet_mesh': None, # (!) real value is '<staticmethod(<built-in method make_tet_mesh of type object at 0x00007FFDC68CE870>)>'
        'make_tri_mesh': None, # (!) real value is '<staticmethod(<built-in method make_tri_mesh of type object at 0x00007FFDC68CE870>)>'
        'materials': None, # (!) real value is "<attribute 'materials' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'nodes': None, # (!) real value is "<attribute 'nodes' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'num_clusters': None, # (!) real value is "<attribute 'num_clusters' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'randomizeConstraints': None, # (!) real value is "<method 'randomizeConstraints' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'randomize_constraints': None, # (!) real value is "<method 'randomize_constraints' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'releaseCluster': None, # (!) real value is "<method 'releaseCluster' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'releaseClusters': None, # (!) real value is "<method 'releaseClusters' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'release_cluster': None, # (!) real value is "<method 'release_cluster' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'release_clusters': None, # (!) real value is "<method 'release_clusters' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'setMass': None, # (!) real value is "<method 'setMass' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'setPose': None, # (!) real value is "<method 'setPose' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'setTotalDensity': None, # (!) real value is "<method 'setTotalDensity' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'setTotalMass': None, # (!) real value is "<method 'setTotalMass' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'setVelocity': None, # (!) real value is "<method 'setVelocity' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'setVolumeDensity': None, # (!) real value is "<method 'setVolumeDensity' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'setVolumeMass': None, # (!) real value is "<method 'setVolumeMass' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'setWindVelocity': None, # (!) real value is "<method 'setWindVelocity' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'set_mass': None, # (!) real value is "<method 'set_mass' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'set_pose': None, # (!) real value is "<method 'set_pose' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'set_total_density': None, # (!) real value is "<method 'set_total_density' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'set_total_mass': None, # (!) real value is "<method 'set_total_mass' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'set_velocity': None, # (!) real value is "<method 'set_velocity' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'set_volume_density': None, # (!) real value is "<method 'set_volume_density' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'set_volume_mass': None, # (!) real value is "<method 'set_volume_mass' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'set_wind_velocity': None, # (!) real value is "<method 'set_wind_velocity' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'unlinkCurve': None, # (!) real value is "<method 'unlinkCurve' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'unlinkGeom': None, # (!) real value is "<method 'unlinkGeom' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'unlinkSurface': None, # (!) real value is "<method 'unlinkSurface' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'unlink_curve': None, # (!) real value is "<method 'unlink_curve' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'unlink_geom': None, # (!) real value is "<method 'unlink_geom' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'unlink_surface': None, # (!) real value is "<method 'unlink_surface' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'wind_velocity': None, # (!) real value is "<attribute 'wind_velocity' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
        'world_info': None, # (!) real value is "<attribute 'world_info' of 'panda3d.bullet.BulletSoftBodyNode' objects>"
    }


