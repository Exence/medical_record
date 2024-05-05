from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session

from models.vac_name import VacNameUpdate, VacNameCreate, VacNamePK, VacNameTypeDict

from models.user import User
from tables import VacName


class VacNameService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_by_pk(self, id: int) -> VacName:
        vac_name = (
            self.session
            .query(VacName)
            .filter_by(id=id)
            .first()
        )

        if not vac_name:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Vac Name is not found'
            )
        return vac_name

    def get_all_vac_names_as_dict(self) -> VacNameTypeDict:
        query = (
            self.session
            .query(VacName)
            .all()
        )

        vac_names = {'prof': {}, 'epid': {}}

        for vac_name in query:
            if vac_name.vac_type == 'Профилактическая':
                vac_names['prof'][vac_name.id] = vac_name.name
            elif vac_name.vac_type == 'По показаниям':
                vac_names['epid'][vac_name.id] = vac_name.name

        return vac_names

    def get_vac_name_by_pk(self, vac_name_pk: VacNamePK) -> VacName:
        return self._get_by_pk(vac_name_pk.id)

    def get_vac_names_by_type(self, vac_type: str) -> list[VacName]:
        return (
            self.session
            .query(VacName)
            .filter_by(vac_type=vac_type)
            .order_by(VacName.name)
            .all()
        )

    def add_new_vac_name(self, user: User, vac_name_data: VacNameCreate):
        if user:
            vac_name = VacName(**vac_name_data.dict())
            self.session.add(vac_name)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return vac_name

    def update_vac_name(self, user: User, vac_name_data: VacNameUpdate):
        if user:
            vac_name = self._get_by_pk(vac_name_data.id)
            for field, value in vac_name_data:
                setattr(vac_name, field, value)
            self.session.commit()
            return vac_name
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

    def delete_vac_name(self, user: User, vac_name_pk: VacNamePK):
        if user:
            vac_name = self._get_by_pk(vac_name_pk.id)
            self.session.delete(vac_name)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
