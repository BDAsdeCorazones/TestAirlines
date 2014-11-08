class CreateAvions < ActiveRecord::Migration
  def change
    execute <<-SQL
      create table avion(
        idAvion serial primary key,
        modelo varchar(6) NOT NULL,
        marca text not null,
        capacidadPrimera int NOT NULL,
        capacidadTurista int NOT NULL,
        disponible varchar(1) check(disponible in ('y', 'n'))
      );

      create or replace function favion() returns trigger as $tavion$
        begin 
          if new.idavion is null then new.idavion = (select max(idavion) from avions) + 1;
          end if;
        return new;
       end;
     $tavion$ language plpgsql;

     create trigger tavion
     before insert on avions
     for each row
     execute procedure favion()
    SQL
  end
end