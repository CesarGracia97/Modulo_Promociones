export interface TariffPlanes {
    TARIFFPLANID: number;
    TARIFFPLAN: string;
}

export interface TariffPlanesVariant {
    TARIFFPLANVARIANTID: number;
    TARIFFPLANVARIANT: string;
}

export interface TariffPlan_X_TariffPlanVariant {
    TARIFFPLANID: number;
    TARIFFPLAN: string;
    TARIFFPLANVARIANTID: number;
    TARIFFPLANVARIANT: string;
}