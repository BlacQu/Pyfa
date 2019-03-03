# ammoTrackingMultiplier
#
# Used by:
# Items from category: Charge (182 of 949)
# Charges from group: Projectile Ammo (128 of 128)
type = "passive"


def handler(fit, module, context):
    module.multiplyItemAttr("trackingSpeed", module.getModifiedChargeAttr("trackingSpeedMultiplier"))
