from datetime import date
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from database import get_session

from models.vac_name import VacNameUpdate, VacNameCreate, VacNamePK, VacNameDict

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
    
    def get_all_vac_names_as_dict(self) -> dict[VacNameDict]:
        query = (
            self.session
            .query(VacName)
            .all()
        )
        vac_names = dict()
        for vac in query:
            vac_names[vac.id] = VacNameDict(name=vac.name,vac_type=vac.vac_type)
        
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
        if user.access_level in ['admin', 'db_admin']:
            vac_name = vac_name(**vac_name_data.dict())
            self.session.add(vac_name)
            self.session.commit()            
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
        return vac_name

    def update_vac_name(self, user: User, vac_name_data: VacNameUpdate):
        if user.access_level in ['admin', 'db_admin']:
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
        if user.access_level in ['admin', 'db_admin']:
            vac_name = self._get_by_pk(vac_name_pk.id)
            self.session.delete(vac_name)
            self.session.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )
